from config.config import RAW_DATA_DIR
from data.csv_loader import CSVLoader

loader = CSVLoader()

df = loader.load(RAW_DATA_DIR / "nifty_5m.csv")

print(df.head())

print(df.dtypes)