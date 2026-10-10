import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.transform import clean_data

def test_negative_amount_removed():

    df = pd.DataFrame({
        "amount": [100, -50, 200],
        "date": ["2025-01-01"] * 3
    })

    result = clean_data(df)

    assert len(result) == 2