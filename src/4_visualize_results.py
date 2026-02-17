import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

# 1. Load data generated from your SQL and Pandas cleaning steps
df = pd.read_csv('data/cleaned_inventory.csv')

# 2. Setup Features and Target for Analysis
X = df[['sales_velocity', 'lead_time']]
y = df['stockout_risk']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Random Forest for Feature Importance Analysis
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

# 4. Set Advanced Seaborn Styling
sns.set_theme(style="whitegrid", palette="viridis")

# 5. Create the 4-in-1 Dashboard
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Inventory Analysis Dashboard', fontsize=22, fontweight='bold')

# --- Panel 1: Correlation Heatmap (Fixed for numeric only) ---
numeric_df = df.select_dtypes(include=['float64', 'int64'])
sns.heatmap(numeric_df.corr(numeric_only=True), annot=True, cmap='RdBu_r', center=0, ax=axes[0, 0])
axes[0, 0].set_title('Feature Correlation: Multi-Variable Analysis')

# --- Panel 2: Sales Velocity Distribution by Risk ---
sns.kdeplot(data=df, x='sales_velocity', hue='stockout_risk', fill=True, ax=axes[0, 1])
axes[0, 1].set_title('Probability Density: Sales vs. Stockout Risk')

# --- Panel 3: Confusion Matrix (Accuracy Analysis) ---
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[1, 0])
axes[1, 0].set_xlabel('Predicted Risk Status')
axes[1, 0].set_ylabel('Actual Risk Status')
axes[1, 0].set_title('Model Confusion Matrix')

# --- Panel 4: Feature Importance (Key Drivers) ---
feat_importances = pd.Series(rf.feature_importances_, index=X.columns)
feat_importances.sort_values().plot(kind='barh', color='teal', ax=axes[1, 1])
axes[1, 1].set_title('Top Drivers of Inventory Stockouts')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('data/advanced_diagnostic_dashboard.png', dpi=300)
print("Advanced 4-in-1 Dashboard saved to data/advanced_diagnostic_dashboard.png!")