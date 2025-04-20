"""
load_data.py

Loads and cleans all tables from a SQLite database in `data/`.
Returns a dict of cleaned pandas DataFrames, keyed by table name.
"""

import os
import sqlite3
import pandas as pd
import re


# Compute base directory (one level up from src/)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DB_PATH = os.path.join(BASE_DIR, 'data', 'score.db')


def load_and_clean(db_path='data/score.db'):
    # 1. Connect to SQLite
    conn = sqlite3.connect(db_path)
    
    # 2. Discover table names
    tables = pd.read_sql_query(
        "SELECT name FROM sqlite_master WHERE type='table';",
        conn
    )['name'].tolist()
    
    cleaned = {}
    
    for tbl in tables:
        # 3a. Load raw table
        df = pd.read_sql_query(f"SELECT * FROM {tbl};", conn)
        
        # 3b. Numeric imputation (median)
        for col in df.select_dtypes(include=['int64','float64']).columns:
            if df[col].isnull().any():
                df[col] = df[col].fillna(df[col].median())

        
        # 3c. Categorical fill (mode or 'Unknown')
        for col in df.select_dtypes(include=['object']).columns:
            if df[col].isnull().any():
                mode_vals = df[col].mode()
                fill_val = mode_vals.iloc[0] if not mode_vals.empty else 'Unknown'
                df[col].fillna(fill_val, inplace=True)
        
        # 3d. Time conversion for HH:MM strings
        for col in df.select_dtypes(include=['object']).columns:
            sample = df[col].dropna().astype(str).head(20)
            if sample.str.match(r'^\d{1,2}:\d{2}$').all():
                df[col] = pd.to_datetime(df[col], format='%H:%M', errors='coerce').dt.time
        
        # 3e. Drop default index column
        if 'index' in df.columns and df['index'].equals(pd.Series(range(len(df)))):
            df.drop(columns=['index'], inplace=True)
        
        # Store the cleaned table
        cleaned[tbl] = df
    
    conn.close()
    return cleaned

if __name__ == '__main__':
    # Quick test when running this script directly:
    tables = load_and_clean()
    print("Loaded and cleaned tables:", list(tables.keys()))
