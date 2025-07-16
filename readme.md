🏦 DeFi Wallet Credit Scoring – Aave V2 Protocol

This project builds a **machine learning-based credit scoring system** that assigns a score between **0–1000** to DeFi wallets based on their historical interaction with the **Aave V2 protocol** on Polygon.

Note: Before Running the Main file(zeru_assignment.ipynb) run Json_to_csv.py for json to csv conversion.

Wallets are categorized as:
- **Good** (Score ≥ 550)
- **Moderate** (550 > Score >= 300)
- **Bad** (Score < 300)

---

## 📁 Project Structure

Json input -> CSV conversion -> Extracting Action Data -> Aggregating Data of wallets -> Creating heuristic credit score for Regression model -> General Graph on dataset -> Train Test Split -> Model training and prediction -> Model evaluation -> choosing best model for sample input prediction

## 🔄 Workflow of the Project

### 1. **Raw Transaction Data (JSON)**
- JSON records from Aave V2 include fields like `actionData`, `userId`, `amount`, etc.

### 2. **Data Extraction**
- Extract only the `actionData` for relevant transactions (`deposit`, `borrow`, `repay`, etc.)
- Convert extracted JSON to CSV using `pandas`.

### 3. **Aggregation by Wallet**
- Group data by `userId`
- Compute meaningful features per wallet:
  - `total_Deposit_usd`
  - `total_Repay_usd`
  - `avg_Borrow_rate`
  - `num_Deposits`, etc.

### 4. **Data Scaling**
- Normalize all numeric features using **MinMaxScaler** (range 0–1)

### 5. **Heuristic Credit Score Function**
- A weighted formula is used to simulate credit behavior:
  ```python
  agg["credit_score"] = (
    0.4 * numeric_df["total_Repay_usd"] +
    0.2 * numeric_df["total_Deposit_usd"] +
    0.15 * numeric_df["num_Deposits"] +
    0.15 * (1-numeric_df["avg_Borrow_rate"]) +  # low borrow rate is good
    0.1 * numeric_df["total_collateral_usd"]
    ) * 2000

  df["credit_score"] = df["credit_score"].clip(0, 1000)

### 6. **Model Training**
-Use RandomForestRegressor to model credit score predictions (based on above features)
-Evaluate using R² metrics

### 7. **Classification**
Based on predicted credit score:

Good → ≥ 500

Risky → 300-500

Bad → < 300

#### Dependencies
Python 
pandas
scikit-learn
numpy