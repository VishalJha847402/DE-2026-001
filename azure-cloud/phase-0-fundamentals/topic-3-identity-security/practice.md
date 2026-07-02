# Practice — Azure Topic 3: Identity & Security

> Hands-on with your own identity + RBAC in the portal, then reasoning drills on
> the OrderIQ platform. Security is a *judgment* skill — every answer must include
> the **why**.

---

## 🛠️ Hands-on 1 — meet your own identity (~3 min)

1. Portal → search **Microsoft Entra ID** → **Users**. Find yourself. You are a
   **user** in your own **tenant**.
2. Open your subscription → **Access control (IAM)** → **Role assignments**. What
   role do you hold, at what scope?

<details><summary>What you should find</summary>

You're typically **Owner** at **subscription scope** — because it's *your personal
account and wallet*. In a company you would never get this; you'd be in a group
like `de-team` with Contributor on specific RGs. Recognizing "I am Owner here, that
is the exception not the norm" is the point.
</details>

---

## 🛠️ Hands-on 2 — grant a scoped role (~5 min)

On the RG from Topic 2 (`rg-orderiq-dev`):

1. Open the RG → **Access control (IAM)** → **+ Add → Add role assignment**.
2. Pick role **Reader**. Assign it to any identity you can (a second Microsoft
   account if you have one; otherwise walk to the final review screen and stop).
3. Note the three things the wizard forced you to choose.

<details><summary>Answer</summary>

Exactly the RBAC triple: **role** (Reader) + **member/who** (the identity) +
**scope** (this RG — chosen implicitly by where you opened IAM). Every grant in
Azure, no exceptions, is these three choices.
</details>

---

## 🟢 Easy 1 — sort the identities

For each, say which identity type fits (user / group / service principal / managed identity):

1. You logging into the portal.
2. The whole analytics team needing GOLD-layer read access.
3. A Python script on a non-Azure server that must call an Azure API.
4. ADF needing to read the dev lake, with zero secrets stored.

<details><summary>Answer</summary>

1. **User.** 2. **Group** (grant once to the group). 3. **Service principal** (it's
outside Azure, so it needs a credential — managed identity isn't available off-Azure).
4. **Managed identity** — ADF is an Azure resource, so Azure can own its robot
credentials. Note the contrast between 3 and 4: managed identity only works *for
Azure resources*.
</details>

---

## 🟢 Easy 2 — the storage-role trap

A teammate has **Contributor** on `storderiqdevlake` but gets
`403 This request is not authorized` reading a file with Spark.

1. Why? (Contributor sounds powerful!)
2. What's the minimal fix for read-only access?

<details><summary>Answer</summary>

1. Contributor manages the **resource** (settings, config) — the **data plane** is
   separate. Reading blobs needs a `Storage Blob Data ...` role.
2. Grant **Storage Blob Data Reader** on that storage account (or a narrower
   container scope). Not Contributor-anything — least privilege.
</details>

---

## 🟡 Medium 1 — design OrderIQ's access matrix

Assign each actor the **smallest role at the narrowest scope**:

| Actor | Needs |
|-------|-------|
| Nightly Databricks job | read bronze, write silver/gold on prod lake |
| Analysts | query gold data only |
| New DE hire | build resources in dev, no prod |
| Auditor | see configurations everywhere, touch nothing |

<details><summary>Model answer</summary>

| Actor | Grant |
|-------|-------|
| Databricks job (**managed identity**) | **Storage Blob Data Contributor** on the prod lake (container-scoped if possible) |
| `analysts` **group** | **Storage Blob Data Reader** on the **gold container only** |
| `de-team` **group** | **Contributor** on `rg-orderiq-dev` only (nothing on prod) |
| `auditors` **group** | **Reader** at **subscription** scope |

Patterns to notice: identities are groups/managed identities (never individuals),
data roles for data, resource roles for building, prod untouched by default.
</details>

---

## 🟡 Medium 2 — Key Vault or not?

Which belong in Key Vault, which are solved by managed identity, which belong in
plain config?

1. Password for an external PostgreSQL (outside Azure) the pipeline reads.
2. Databricks needing to write to ADLS.
3. A third-party weather-API key.
4. The name of the input container (`bronze`).

<details><summary>Answer</summary>

1. **Key Vault** — external system, the secret must exist somewhere; store it in the
   safe, fetch at runtime.
2. **Managed identity** — Azure-to-Azure, no secret should exist at all.
3. **Key Vault** — real secret, external party.
4. **Plain config** — not a secret; container names, paths, flags go in normal
   parameters/config. Don't clutter the safe with non-secrets.
</details>

---

## 🔴 Hard — incident drill: the leaked connection string

**Scenario:** An OrderIQ engineer pasted the storage account's **connection string**
(a full-access key) into a notebook, which got pushed to a public GitHub repo. A
scraper found it within minutes.

1. What can the attacker do with it? How is this worse than a leaked *user password*?
2. Immediate containment — first two actions, in order?
3. Redesign so this class of leak is **impossible**: name the mechanism for each
   connection in `ADF → Databricks → ADLS + external Postgres`, and where the one
   real secret lives.
4. In the new design, what would the *same mistake* (pushing the notebook) leak?

<details><summary>Answers</summary>

1. The connection string is a **key to the whole storage account** — full read/write
   /delete on all containers, **no MFA, no identity, no RBAC evaluation**, and the
   access looks like legitimate key usage. A user password at least belongs to an
   identity (MFA, conditional access, RBAC-limited) and its use is attributable.
2. **(1) Rotate/regenerate the storage keys** — kills the leaked credential
   instantly. **(2) Purge the secret from the repo/history and audit access logs**
   for what was touched while it was live. (Rotate first — every minute it's valid,
   data is exposed.)
3. Target design:
   - ADF → Databricks: **managed identity** (ADF's).
   - Databricks → ADLS: **cluster's managed identity** + `Storage Blob Data
     Contributor` scoped to the needed containers.
   - Databricks → external Postgres: password kept in **Key Vault**, read at runtime
     via `dbutils.secrets.get()` using the workspace's managed identity.
   - Storage **account keys disabled** (Azure lets you disallow key-based auth) so
     no connection string even works.
4. The notebook now contains only code like
   `dbutils.secrets.get(scope="orderiq-kv", key="postgres-password")` — pushing it
   leaks a *reference to* a secret, not the secret. The attacker gets a string that
   is useless without being an authorized identity inside your tenant. That's the
   whole point of the design: the mistake still happens; the damage doesn't.
</details>

---

### ✅ Mastery check for Topic 3

Without notes:

- explain the two gates (authentication vs authorization) and where Entra/RBAC sit,
- write an RBAC grant as who + role + scope, with least privilege,
- explain when managed identity applies vs Key Vault vs plain config,
- and walk the leaked-credential incident: contain, then redesign so it can't recur.

Passed? → **Topic 4 — The Azure Data Stack Map** (ADLS + ADF + Databricks + Synapse
+ Fabric in one picture) — finishes Phase 0.

*Back to the [lesson](./README.md).*
