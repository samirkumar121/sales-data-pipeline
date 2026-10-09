def validate_data(df):

    if df["order_id"].isnull().sum() > 0:
        raise ValueError("Order ID contains null values")

    if (df["amount"] < 0).any():
        print("Warning: Negative amounts found")

    print("Data Quality Checks Passed")