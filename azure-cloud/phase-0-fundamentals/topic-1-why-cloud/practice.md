# Practice — Azure Topic 1: Why Cloud

> Azure is a **hands-on** skill. This lesson is conceptual, so practice = (1) a
> real one-time account setup you'll use all series, and (2) reasoning drills that
> make compute/storage separation and elasticity concrete. Explain *why*, not just *what*.

---

## 🛠️ One-time setup — your free Azure account (do this now, ~10 min)

You'll need this for every hands-on Azure lesson from Phase 1 onward.

1. Go to **portal.azure.com** → **Start free** → sign in with a Microsoft account.
2. You get **₹/$200 free credit for 30 days** + many services free for 12 months.
   (A card is required for identity; you won't be charged unless you upgrade.)
3. Once in, open the **portal**. In the top search bar, type each of these and just
   *look* (don't create yet): **Storage accounts**, **Azure Databricks**,
   **Data Factory**, **Synapse Analytics**.
4. Also open **fabric.microsoft.com** → start the **free Fabric trial** (separate
   from Azure; we use it in Phase 4).

> ✅ Ready when you can reach the Azure portal home and see the service search work.
> 🔒 **Cost safety:** we'll always tell you to *stop/delete* compute after labs.
> Storage is cheap; compute left running is what burns credit.

---

## 🟢 Easy 1 — spot storage vs compute

For each Azure service, say **storage** or **compute**, and one line why:

1. Azure Data Lake Storage Gen2
2. Azure Databricks cluster
3. OneLake
4. Synapse Spark pool

<details><summary>Answer</summary>

1. **Storage** — holds files (the lake), always on, cheap.
2. **Compute** — an engine that reads storage and processes data; turn on/off.
3. **Storage** — Fabric's unified lake storage.
4. **Compute** — Spark engine that processes data from storage.

The skill: reading any Azure diagram and instantly sorting boxes into "holds data"
vs "processes data."
</details>

---

## 🟢 Easy 2 — rent vs buy math

OrderIQ needs 100 machines for 6 hours, once a week.

1. On-prem: how many machine-hours do you *pay for* per year (buying 100 machines)?
2. Cloud: how many machine-hours do you *pay for* per year (rent only when used)?
3. Roughly how many times more wasteful is on-prem here?

<details><summary>Answer</summary>

1. On-prem: 100 machines × 24 h × 365 = **876,000 machine-hours/year** paid (used or not).
2. Cloud: 100 × 6 h × 52 weeks = **31,200 machine-hours/year** paid.
3. 876,000 / 31,200 ≈ **28× less waste** with cloud (and that ignores maintenance,
   power, cooling, and upfront CapEx).
</details>

---

## 🟡 Medium 1 — design the OrderIQ nightly job the cloud way

Describe, in 4–6 lines, how you'd run OrderIQ's nightly bronze→silver→gold ETL so
that you pay as little as possible. Name what stays on 24/7 and what turns off.

<details><summary>Model answer</summary>

- **Storage (ADLS/OneLake):** always on, holds all 8 TB of order history — cheap.
- **Compute (Databricks cluster):** scheduled to **start at 2 AM**, read yesterday's
  data from storage, run the medallion transforms, write results back to storage,
  then **auto-terminate**.
- You pay ~40 min of compute/day + always-on cheap storage — not 24 h of servers.
- This is only possible because compute and storage are **separated**: the data
  survives in storage while compute is off.
</details>

---

## 🟡 Medium 2 — service-model sorting

Label each as IaaS, PaaS, or SaaS:

1. You rent a bare Azure VM and `pip install pyspark` yourself.
2. You use Azure Databricks — Azure runs the platform, you write notebooks.
3. You use Microsoft Fabric — you just build lakehouses/reports, no infra.

<details><summary>Answer</summary>

1. **IaaS** — you manage OS, runtime, app.
2. **PaaS** — provider manages the platform; you bring code/data.
3. **SaaS** — you only bring your data/usage; everything else is managed.

Most Azure DE work = **PaaS**; Fabric moves it toward **SaaS**.
</details>

---

## 🔴 Hard — BREAK it: reason through the on-prem failure, then design the cloud fix

**Break-it scenario:** OrderIQ runs on-prem with a fixed 20-machine cluster where
storage and compute are fused. Two things happen the same week:
(A) order history grows from 6 TB to 9 TB, and (B) Black Friday brings a 20× query spike.

1. On the fused on-prem cluster, why does growth (A) *force* you to also add
   processing power you may not need — and vice versa for spike (B)?
2. What breaks on Black Friday, and what's the only on-prem "fix" (and its cost)?
3. **Design the cloud version:** how do compute/storage separation + elasticity
   solve **both** (A) and (B) independently and cheaply? Be specific about which
   layer changes for each.

<details><summary>Answers</summary>

1. Because storage and compute live on the **same machines**. To store the extra
   3 TB (A) you must add machines — which drags in processing power you didn't ask
   for. To handle the spike (B) you must add machines — which drags in storage you
   didn't need. The two are chained together; you can't grow one without the other.
2. On Black Friday the fixed 20-machine cluster is overwhelmed → queries queue,
   time out, pipeline SLAs blow. The only on-prem fix is to **permanently buy**
   enough machines for peak (say 100) — paying for 80 idle machines the other 360
   days.
3. Cloud, separated:
   - **(A) data growth →** grow only the **storage** layer (ADLS scales on its own,
     cheaply). Compute untouched.
   - **(B) query spike →** autoscale only the **compute** layer (5 → 100 nodes for
     the evening, back to 5 at midnight). Storage untouched.
   Each problem is solved in its own layer, and you pay for the extra compute for
   only a few hours. That independence is the entire payoff of separation +
   elasticity.
</details>

---

### ✅ Mastery check for Topic 1

Without notes:

- explain compute/storage separation and why idle is nearly free in cloud,
- give the rent-vs-buy reason on-prem wastes money on spiky workloads,
- sort Azure services into storage vs compute, and IaaS/PaaS/SaaS,
- and explain how separation + elasticity solve data-growth and spike independently.

Passed? → **Topic 2 — Azure Basics** (subscriptions, resource groups, regions, and
the cost model you'll live inside).

*Back to the [lesson](./README.md).*
