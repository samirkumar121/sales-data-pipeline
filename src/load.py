def load_to_sqlite(df, db_path):

    conn = sqlite3.connect(db_path)

    try:

        existing = pd.read_sql(
            "SELECT order_id FROM sales",
            conn
        )

        df = df[
            ~df["order_id"].isin(
                existing["order_id"]
            )
        ]

    except:
        pass

    df.to_sql(
        "sales",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()

    print(f"Loaded {len(df)} new records")