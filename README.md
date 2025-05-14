# Student Performance Prediction Pipeline

## Project Overview and Objective
I built an end‑to‑end machine learning workflow that takes raw student data (`score.db`), cleans it, explores key patterns in a Jupyter Notebook, trains a Random Forest model, and evaluates its performance.  
**Why:** Helps educators understand which factors (study hours, attendance, etc.) most impact O‑Level math scores and target support where it’s needed.

## Deliverables
- **eda.ipynb** — Visual and statistical exploration of the dataset  
- **src/** — Four Python scripts for data loading, preprocessing, training, and evaluation  
- **requirements.txt** — Exact package versions for reproducibility  
- **run.sh** — Single‑command script to execute the full workflow

## Repository Setup

### 1. Created a GitHub repository
1. Log in to GitHub as rush2priyanka.  
2. Click New and name the repo Student_Performance_Prediction_Pipeline  
3. Set Visibility to Public.
4. Click Create repository.

### 2. Cloneed and pushed code
```bash
git clone git@github.com:rush2priyanka/Challenge_1.git
cd Challenge_1

# Copied local files into this folder, then:
git add .
git commit -m "Initial commit: add EDA, src/, requirements, run.sh, README"
git push
