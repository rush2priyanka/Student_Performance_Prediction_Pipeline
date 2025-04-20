"""
preprocess.py

Loads cleaned data, splits into features/target, encodes categoricals,
and writes train/test CSVs to data/processed/.
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from load_data import load_and_clean, DB_PATH

def preprocess(db_path=None, test_size=0.2, random_state=42):
    # 1. Load and clean tables
    path = db_path or DB_PATH
    tables = load_and_clean(path)

    # 2. Select the first table dynamically
    main_table = list(tables.keys())[0]
    df = tables[main_table]
    print(f"Preprocessing table: {main_table}")

    # 3. Choose 'final_test' as target if present
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    target = 'final_test' if 'final_test' in numeric_cols else numeric_cols[0]
    print(f"Using target column: {target}")

    # 4. Separate features and target
    X = df.drop(columns=[target])
    y = df[target]

    # 5. One‑hot encode categorical variables
    X = pd.get_dummies(X, drop_first=True)
    print(f"Encoded {X.shape[1]} features")

    # 6. Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    print(f"Split data: {len(X_train)} train rows, {len(X_test)} test rows")

    # 7. Prepare output directory
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    out_dir = os.path.join(base_dir, 'data', 'processed')
    os.makedirs(out_dir, exist_ok=True)

    # 8. Save train/test files
    for name, df_part in [
        ('X_train', X_train),
        ('X_test',  X_test),
        ('y_train', y_train),
        ('y_test',  y_test)
    ]:
        file_path = os.path.join(out_dir, f"{name}.csv")
        df_part.to_csv(file_path, index=False)

    print(f"Processed files saved to: {out_dir}")
    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    preprocess()
