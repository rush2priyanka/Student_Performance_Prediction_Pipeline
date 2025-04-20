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
1. Logged in to GitHub and click **“New repository.”**  
2. Named it `Challenge_1` and set it to **Private**.  
3. Click **Create repository**.

### 2. Add collaborators
- Go to **Settings → Manage access → Invite a collaborator**  
- Invite:
  - `waseemga`
  - `khammingfatt-analytico`

### 3. Clone and push your code
```bash
git clone git@github.com:<your-username>/Challenge_1.git
cd Challenge_1

# Copy your local files into this folder, then:
git add .
git commit -m "Initial commit: add EDA, src/, requirements, run.sh, README"
git push
