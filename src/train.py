print(">>> train.py is starting…")

"""
train.py

Loads processed data, trains a Random Forest model (50 trees),
evaluates it, and saves the model to disk.
"""

import os
import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def train_model(processed_dir=None, model_path=None):
    # 1. Locate processed data folder
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    data_dir = processed_dir or os.path.join(base_dir, 'data', 'processed')
    print(f"Loading data from: {data_dir}")

    # 2. Read CSVs
    print("Reading train/test datasets…")
    X_train = pd.read_csv(os.path.join(data_dir, 'X_train.csv'))
    X_test  = pd.read_csv(os.path.join(data_dir, 'X_test.csv'))
    y_train = pd.read_csv(os.path.join(data_dir, 'y_train.csv')).squeeze()
    y_test  = pd.read_csv(os.path.join(data_dir, 'y_test.csv')).squeeze()
    print(f"Shapes: X_train={X_train.shape}, X_test={X_test.shape}")

    # 3. Instantiate the model
    model = RandomForestRegressor(n_estimators=50, random_state=42)

    # 4. Train
    print("Starting model training…")
    model.fit(X_train, y_train)
    print("Model training complete.")

    # 5. Predict and evaluate
    print("Evaluating model…")
    preds = model.predict(X_test)

    # Compute RMSE manually
    mse  = mean_squared_error(y_test, preds)
    rmse = np.sqrt(mse)
    r2   = r2_score(y_test, preds)

    print(f"Test RMSE: {rmse:.2f}")
    print(f"Test R²:   {r2:.2f}")

    # 6. Save the trained model
    out_file = model_path or os.path.join(base_dir, 'src', 'random_forest.pkl')
    joblib.dump(model, out_file)
    print(f"Model saved to: {out_file}")

    return model

if __name__ == '__main__':
    train_model()
