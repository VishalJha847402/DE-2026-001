#!/usr/bin/env python3
"""
OrderIQ — e-commerce dataset generator (v1: core tables).

Stdlib only — NO installs needed to GENERATE (DuckDB is only needed later to load).
Referential integrity guaranteed. Includes deliberate messiness (nulls, a few exact
duplicate order rows) so the data-quality / dedup practice problems are real.

Usage:
    python generate.py --orders 100000 --out ./data     # full (~100k orders)
    python generate.py --orders 1000                     # quick test
Then:
    pip install duckdb && python seed_duckdb.py

Tables produced (CSV): customers, products, sellers, orders, order_items, payments
"""
import argparse
import csv
import os
import random
import datetime as dt

random.seed(42)  # reproducible

CITIES = [("Mumbai", "MH"), ("Delhi", "DL"), ("Bangalore", "KA"), ("Hyderabad", "TG"),
          ("Chennai", "TN"), ("Kolkata", "WB"), ("Pune", "MH"), ("Ahmedabad", "GJ"),
          ("Jaipur", "RJ"), ("Lucknow", "UP"), ("Surat", "GJ"), ("Indore", "MP")]
CATEGORIES = ["Electronics", "Books", "Fashion", "Home", "Beauty", "Toys", "Grocery", "Sports"]
PAY_TYPES = ["credit_card", "debit_card", "upi", "wallet", "cod"]
STATUSES = ["delivered"] * 6 + ["shipped"] * 2 + ["cancelled", "returned"]  # weighted
FIRST = ["Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Ananya", "Diya",
         "Isha", "Priya", "Neha", "Rohan", "Kabir", "Ishaan", "Zara"]
LAST = ["Sharma", "Verma", "Iyer", "Nair", "Reddy", "Patel", "Singh", "Gupta",
        "Jha", "Das", "Rao", "Khan"]


def rand_date(a, b):
    return a + dt.timedelta(days=random.randint(0, (b - a).days))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--orders", type=int, default=100_000)
    ap.add_argument("--out", default="./data")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    N = args.orders
    n_cust = max(10, N // 3)
    n_prod = 500
    n_sell = 60
    d0, d1 = dt.date(2023, 1, 1), dt.date(2025, 12, 31)

    # ---------- products ----------
    prods = []  # (product_id, price)
    with open(os.path.join(args.out, "products.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["product_id", "product_name", "category", "price", "weight_g"])
        for i in range(1, n_prod + 1):
            pid = f"P{i:04d}"
            cat = random.choice(CATEGORIES)
            price = round(random.uniform(99, 4999), 2)
            prods.append((pid, price))
            w.writerow([pid, f"{cat} Item {i}", cat, price, random.randint(50, 5000)])

    # ---------- sellers ----------
    sellers = []
    with open(os.path.join(args.out, "sellers.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["seller_id", "seller_name", "city", "state"])
        for i in range(1, n_sell + 1):
            sid = f"S{i:03d}"
            c = random.choice(CITIES)
            sellers.append(sid)
            w.writerow([sid, f"Seller {i}", c[0], c[1]])

    # ---------- customers (messiness: ~1% null email, ~1% null city) ----------
    custs = []
    with open(os.path.join(args.out, "customers.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["customer_id", "name", "email", "city", "state", "signup_date"])
        for i in range(1, n_cust + 1):
            custs.append(i)
            c = random.choice(CITIES)
            name = f"{random.choice(FIRST)} {random.choice(LAST)}"
            email = "" if random.random() < 0.01 else f"user{i}@example.com"
            city = "" if random.random() < 0.01 else c[0]
            state = "" if city == "" else c[1]
            w.writerow([i, name, email, city, state, rand_date(d0, d1).isoformat()])

    # ---------- orders + order_items + payments (streamed) ----------
    fo = open(os.path.join(args.out, "orders.csv"), "w", newline="")
    fi = open(os.path.join(args.out, "order_items.csv"), "w", newline="")
    fp = open(os.path.join(args.out, "payments.csv"), "w", newline="")
    wo, wi, wp = csv.writer(fo), csv.writer(fi), csv.writer(fp)
    wo.writerow(["order_id", "customer_id", "order_date", "status"])
    wi.writerow(["order_item_id", "order_id", "product_id", "seller_id", "quantity", "unit_price", "freight"])
    wp.writerow(["payment_id", "order_id", "payment_type", "installments", "amount"])

    dup_orders = []   # a few EXACT duplicate order rows appended at the end (for dedup practice)
    item_id = 0
    for oid in range(1, N + 1):
        cid = random.choice(custs)
        odate = rand_date(d0, d1)
        status = "" if random.random() < 0.01 else random.choice(STATUSES)  # ~1% null status
        wo.writerow([oid, cid, odate.isoformat(), status])

        total = 0.0
        for _ in range(random.randint(1, 4)):
            item_id += 1
            pid, price = random.choice(prods)
            sid = random.choice(sellers)
            qty = random.randint(1, 3)
            freight = "" if random.random() < 0.005 else round(random.uniform(20, 120), 2)  # ~0.5% null freight
            wi.writerow([item_id, oid, pid, sid, qty, price, freight])
            total += price * qty + (0.0 if freight == "" else freight)

        wp.writerow([oid, oid, random.choice(PAY_TYPES), random.randint(1, 6), round(total, 2)])

        if len(dup_orders) < 50 and random.random() < 0.001:
            dup_orders.append([oid, cid, odate.isoformat(), status])

    for d in dup_orders:      # append exact duplicate order rows
        wo.writerow(d)

    fo.close(); fi.close(); fp.close()

    print(f"✅ Generated in '{args.out}/':")
    print(f"   customers ~{n_cust} | products {n_prod} | sellers {n_sell}")
    print(f"   orders {N} (+{len(dup_orders)} exact-duplicate rows) | order_items ~{item_id} | payments {N}")
    print("   Deliberate messiness: ~1% null email/city/status, ~0.5% null freight, ~50 dup order rows.")
    print("\nNext:  pip install duckdb  &&  python seed_duckdb.py")


if __name__ == "__main__":
    main()
