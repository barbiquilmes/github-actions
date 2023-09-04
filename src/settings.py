import os
from pathlib import Path

BASE_PATH = os.path.abspath(Path(__file__).parents[1])

SRC_PATH = os.path.join(BASE_PATH, "src")
DATA_PATH = os.path.join(BASE_PATH, "data")

if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)
