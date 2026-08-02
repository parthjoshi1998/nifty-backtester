from pathlib import Path

import pandas as pd

from utils.logger import logger


class CSVLoader:
    """
    Responsible for loading OHLC market data from CSV files.
    """

    # Mandatory columns required for every backtest
    REQUIRED_COLUMNS = [
        "date",
        "open",
        "high",
        "low",
        "close"
    ]

    # Optional columns used by specific strategies/indicators
    OPTIONAL_COLUMNS = [
        "volume",
        "oi"
    ]

    def load(self, file_path: str | Path) -> pd.DataFrame:
        """
        Load OHLC data from CSV.

        Parameters
        ----------
        file_path : str | Path
            Path to CSV file.

        Returns
        -------
        pd.DataFrame
            Cleaned and chronologically sorted DataFrame.
        """

        file_path = Path(file_path)

        logger.info(f"Loading CSV: {file_path}")

        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"{file_path} not found.")

        # Read CSV
        df = pd.read_csv(file_path)

        # Normalize column names
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
        )

        logger.info(f"Columns detected: {list(df.columns)}")

        # Validate required columns
        missing_columns = [
            column
            for column in self.REQUIRED_COLUMNS
            if column not in df.columns
        ]

        if missing_columns:
            logger.error(f"Missing required columns: {missing_columns}")
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

        # Detect optional columns
        available_optional = [
            column
            for column in self.OPTIONAL_COLUMNS
            if column in df.columns
        ]

        logger.info(f"Optional columns detected: {available_optional}")

        # Convert date column to datetime
        df["datetime"] = pd.to_datetime(df["date"])

        # Sort chronologically
        df = (
            df.sort_values("datetime")
            .reset_index(drop=True)
        )

        logger.info(f"Successfully loaded {len(df)} candles.")

        return df