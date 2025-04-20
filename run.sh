#!/usr/bin/env bash
# Activate venv (macOS/Linux)
source .venv/bin/activate

# If you're on Windows PowerShell instead, comment the above line and uncomment:
# .\.venv\Scripts\activate

python src/preprocess.py
python src/train.py
python src/evaluate.py
