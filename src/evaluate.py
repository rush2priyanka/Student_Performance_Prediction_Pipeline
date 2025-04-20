"""
evaluate.py

Loads a trained model and processed test data,
generates predictions, and prints evaluation metrics.
"""

import os
import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

def evaluate(processed_dir=None, model_file=None):
    # 1. Locate files
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    data_dir = processed_dir or os.path.join(base_dir, 'data', 'processed')
    model_path = model_file or os.path.join(base_dir, 'src', 'random_forest.pkl')
    print(f"Loading model from: {model_path}")
    print(f"Loading test data from: {data_dir}")

    # 2. Load model and test set
    model = joblib.load(model_path)
    X_test = pd.read_csv(os.path.join(data_dir, 'X_test.csv'))
    y_test = pd.read_csv(os.path.join(data_dir, 'y_test.csv')).squeeze()

    # 3. Predict
    print("Generating predictions…")
    preds = model.predict(X_test)

    # 4. Compute metrics
    mse  = mean_squared_error(y_test, preds)
    rmse = np.sqrt(mse)
    r2   = r2_score(y_test, preds)

    # 5. Report
    print(f"Final Evaluation on Test Set:")
    print(f"  RMSE: {rmse:.2f}")
    print(f"  R²:   {r2:.2f}")

if __name__ == '__main__':
    evaluate()
