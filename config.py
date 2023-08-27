import os
from pathlib import Path

QUERIES_PATH = Path(__file__).resolve().parent / 'database' / 'quries.sql'
DB_CONNECT = f"postgresql://postgres:{os.getenv('pgAdmin')}@localhost:5432/hh_parser"

EMPLOYER_MAP = {
    "РутКод": 8642172,
    "AVC": 1626408,
    "МЕТИНВЕСТ": 2596438,
    "ФИНТЕХ": 2324020,
    "ОКБ": 2129243,
    "РусЭкспресс": 1875694,
    "IPChain": 3151408,
    "Wanted": 5174849,
    "AERODISK": 2723603,
    "Латера": 1050345,
    "Qualitica": 4181561,
}

