# src/report.py

def generate_report(df):

    report = (
        df.groupby("product")
        ["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print(report)