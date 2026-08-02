from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data Directories
RAW_DATA_DIR = PROJECT_ROOT / "datasets" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "datasets" / "processed"

# Log Directory
LOG_DIR = PROJECT_ROOT / "logs"
LOG_FILE = LOG_DIR / "backtester.log"