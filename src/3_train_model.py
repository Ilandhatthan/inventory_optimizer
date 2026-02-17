import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Load the dataset
df = pd.read_csv('data/cleaned_inventory.csv')

# 2. Select Features (Inputs) and Target (Output)
# We use price, lead time, velocity, and stock to predict the risk
X = df[['price', 'lead_time', 'sales_velocity', 'current_stock']]
y = df['stockout_risk']

# 3. Split the data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and Train the Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. Make Predictions and Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("--- Results ---")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nDetailed Report:")
print(classification_report(y_test, predictions))