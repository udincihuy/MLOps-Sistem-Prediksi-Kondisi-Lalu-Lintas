import pandas as pd

def test_processed_data():
    data = pd.read_csv("data/processed.csv")

    assert not data.empty
    assert "lag1" in data.columns
    assert "lag2" in data.columns
    assert "target" in data.columns