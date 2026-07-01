#!/usr/bin/env python3
"""
Load the generated OrderIQ CSVs into a DuckDB database file.

Usage:
    pip install duckdb
    python seed_duckdb.py            # reads ./data, writes orderiq.duckdb
    python seed_duckdb.py ./data ./orderiq.duckdb

Then query it (Python):
    import duckdb
    con = duckdb.connect("orderiq.duckdb")
    con.sql("SELECT city, COUNT(*) FROM customers GROUP BY city").show()

Or in a notebook cell:
    %pip install duckdb
    import duckdb; con = duckdb.connect("orderiq.duckdb")
"""
import sys
import duckdb

TABLES = ["customers", "products", "sellers", "orders", "order_items", "payments"]


def main():
    data_dir = sys.argv[1] if len(sys.argv) > 1 else "./data"
    db_path = sys.argv[2] if len(sys.argv) > 2 else "orderiq.duckdb"

    con = duckdb.connect(db_path)
    for t in TABLES:
        path = f"{data_dir}/{t}.csv"
        # sample_size=-1 => scan whole file so messy columns infer sensibly
        con.execute(
            f"CREATE OR REPLACE TABLE {t} AS "
            f"SELECT * FROM read_csv_auto('{path}', header=true, sample_size=-1)"
        )
        n = con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        print(f"  loaded {t:<12} {n:>10,} rows")
    con.close()
    print(f"\n✅ Done. Database: {db_path}")
    print("   Try:  import duckdb; duckdb.connect('orderiq.duckdb').sql("
          "'SELECT city, COUNT(*) c FROM customers GROUP BY 1 ORDER BY 2 DESC').show()")


if __name__ == "__main__":
    main()
