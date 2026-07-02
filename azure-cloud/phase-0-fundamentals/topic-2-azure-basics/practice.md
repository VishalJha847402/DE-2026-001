# Practice — Azure Topic 2: Structure & Cost Model

> Hands-on in your free Azure account + reasoning drills. The habits here (RG per
> project, budget alert, tags, auto-terminate) are what keep you off finance's radar.
> Explain *why*, not just *what*.

---

## 🛠️ Hands-on 1 — create your first Resource Group (do this, ~5 min)

In the Azure portal (portal.azure.com):

1. Search **Resource groups** → **+ Create**.
2. Subscription: your free one. Name: `rg-orderiq-dev`. Region: **Central India**.
3. On the **Tags** tab add: `project = orderiq`, `env = dev`. → **Review + create**.
4. Open the new RG. Note it's empty — it's a *folder*, no cost by itself.

> ✅ Done when `rg-orderiq-dev` shows in your Resource groups list with the two tags.
> Keep it — Phase 1 puts a storage account inside it.

---

## 🛠️ Hands-on 2 — set a budget alert (the habit that saves you)

1. Search **Cost Management + Billing** → **Budgets** → **+ Add**.
2. Scope: your subscription. Amount: e.g. **₹500** (or $5). Alert at **80%**.
3. Add your email. Create.

> ✅ Done when a budget exists that will email you before you burn your free credit.

---

## 🟢 Easy 1 — place the resource

Fill the four coordinates every Azure resource must have, for a storage account
named `storderiqdevlake`:

1. Tenant? 2. Subscription? 3. Resource Group? 4. Region?

<details><summary>Answer</summary>

1. Your org's Entra tenant. 2. `OrderIQ-Dev` subscription (the wallet). 3.
`rg-orderiq-dev` (project folder). 4. Central India (co-located with compute).
No resource can exist without all four — there's no "floating" resource.
</details>

---

## 🟢 Easy 2 — what does deleting the RG do?

You delete `rg-orderiq-dev`, which contains a storage account, a Databricks
workspace, and a Data Factory.

1. What happens to the three resources?
2. Why is this behaviour actually *useful* for a DE?

<details><summary>Answer</summary>

1. All three are deleted together — the RG is a shared-lifecycle container.
2. One-click teardown of a whole environment (dev/test). Spin up, experiment, delete
   the RG → everything (and its cost) is gone. No orphaned resources quietly billing.
</details>

---

## 🟡 Medium 1 — the co-location trap

OrderIQ's data lake is in **Central India**. A teammate creates the Databricks
cluster in **East US** because "it was the default."

1. Name the two concrete problems this causes on every job.
2. What's the fix?

<details><summary>Answer</summary>

1. (a) **Slow** — every job pulls TBs across regions/continents (high latency).
   (b) **Costly** — cross-region data movement incurs **egress/transfer charges** on
   every run.
2. Recreate the cluster in **Central India**, same region as the lake. Co-locate
   compute and storage: fast + no cross-region transfer fees.
</details>

---

## 🟡 Medium 2 — read the cost model

Say what you're charged for (a lot / a little / usually free), and why:

1. A Databricks cluster running 24×7 doing nothing.
2. 8 TB sitting in ADLS.
3. Loading 500 GB *into* Azure from your source (ingress).
4. Exporting 500 GB *out* of Central India to another region (egress).

<details><summary>Answer</summary>

1. **A lot** — compute bills per second *while running*, idle or not. This is the #1
   surprise-bill cause. Auto-terminate fixes it.
2. **A little** — storage is cheap per GB/month, but always-on.
3. **Usually free** — ingress into the cloud is typically free.
4. **Costs money** — egress (data leaving a region/cloud) is charged.
</details>

---

## 🔴 Hard — BREAK it: diagnose a ₹40,000 surprise bill, then prevent it

Month-end, OrderIQ-Dev's bill is ₹40,000 — 10× expected. You investigate.

Findings: (1) a Databricks cluster with **no auto-terminate** ran 24×7 all month;
(2) a nightly job reads the Central-India lake from an **East US** cluster; (3)
resources are spread across 3 RGs with **no tags**, so finance can't tell which
project spent what.

1. Rank the three findings by likely cost impact and explain each.
2. Give the specific fix for each.
3. What **three day-one habits** would have prevented the whole situation — and how
   would each have caught it early?

<details><summary>Answers</summary>

1. **Biggest: (1) the always-on cluster** — compute billed every second for a full
   month while mostly idle. Dwarfs the rest. **Second: (2) cross-region egress** —
   every nightly run ships data East US ↔ Central India, paying transfer fees each
   time. **Third: (3) no tags** — not a direct charge, but it *hid* the problem
   (nobody could attribute spend), so it ran unnoticed.
2. (1) Turn on **auto-terminate** (e.g. 20 min idle) — and shut clusters after labs.
   (2) Recreate the cluster in **Central India** to co-locate with the lake (kills
   egress + speeds jobs). (3) **Tag** every resource (`project`, `env`) so Cost
   Management can break spend down.
3. Day-one habits: **(a) budget + alert** → you'd have gotten an 80% email in week
   one instead of a month-end shock. **(b) auto-terminate on all compute** → the
   idle cluster never runs overnight. **(c) tags on everything** → the bill is
   filterable by project/env, so the culprit is obvious in minutes. Together these
   turn a ₹40k surprise into a ₹-few-hundred, fully-explainable spend.
</details>

---

### ✅ Mastery check for Topic 2

Without notes:

- draw Tenant → Subscription → RG → Resource and say what each boundary is for,
- explain why you co-locate compute and storage in one region,
- name what compute vs storage vs egress cost, and why idle compute is the top trap,
- and list the three day-one cost habits (auto-terminate, budget alerts, tags).

Passed? → **Topic 3 — Identity & Security** (Entra ID, RBAC, Managed Identities,
Key Vault): who is allowed to touch these resources.

*Back to the [lesson](./README.md).*
