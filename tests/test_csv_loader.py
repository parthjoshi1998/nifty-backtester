from data.csv_loader import CSVLoader
from config.config import RAW_DATA_DIR


def test_csv_loader():
    loader = CSVLoader()

    df = loader.load(RAW_DATA_DIR / "nifty_5m.csv")

    assert len(df) > 0
    assert "datetime" in df.columns
    assert "open" in df.columns
    assert "close" in df.columns