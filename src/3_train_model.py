import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, mean_absolute_error, r2_score

# 1. Load Data
df = pd.read_csv('data/cleaned_inventory.csv')

# 2. Setup Features and Targets
X = df[['sales_velocity', 'lead_time']]
y_class = df['stockout_risk']  # For Classification
y_reg = df['sales_velocity']   # For Regression

# 3. Train/Test Split (Stable Seed)
X_train, X_test, y_train, y_test = train_test_split(X, y_class, test_size=0.2, random_state=42)
X_train_r, X_test_r, yr_train, yr_test = train_test_split(X, y_reg, test_size=0.2, random_state=42)

# --- [1] LOGISTIC REGRESSION ---
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
log_y_pred = log_model.predict(X_test)

# --- [2] RANDOM FOREST CLASSIFIER ---
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_y_pred = rf_model.predict(X_test)

# --- [3] LINEAR REGRESSION ---
lin_model = LinearRegression()
lin_model.fit(X_train_r, yr_train)
lin_y_pred = lin_model.predict(X_test_r)

# --- THE FULL TERMINAL REPORT ---
print("\n" + "="*50)
print("                     REPORT")
print("="*50)

print("\n[1] LOGISTIC REGRESSION (Baseline Classification)")
print(f"Accuracy: {accuracy_score(y_test, log_y_pred):.2%}")
print(classification_report(y_test, log_y_pred, zero_division=0))

print("\n[2] RANDOM FOREST (Advanced Ensemble Classification)")
print(f"Accuracy: {accuracy_score(y_test, rf_y_pred):.2%}")
print(classification_report(y_test, rf_y_pred, zero_division=0))

print("\n[3] LINEAR REGRESSION (Sales Volume Forecasting)")
print(f"R² Score (Variance Explained): {r2_score(yr_test, lin_y_pred):.4f}")
print(f"Mean Absolute Error: {mean_absolute_error(yr_test, lin_y_pred):.4f}")
print("="*50)