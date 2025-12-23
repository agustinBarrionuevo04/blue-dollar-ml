"""
Centralized project configuration such as common filesystem paths.

Keeping the paths in one file avoids spreading hard-coded absolute
references throughput the code base and makes it simpler to reuse the
processing and training utilities from notebooks or scripts.
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

