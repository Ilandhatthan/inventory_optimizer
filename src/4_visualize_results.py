import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# 1. Load the cleaned data
df = pd.read_csv('data/cleaned_inventory.csv')

# Set professional technical style
sns.set_theme(style="white")
fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.suptitle('Inventory Optimization: Model Diagnostic Dashboard', fontsize=22, fontweight='bold')

# --- PLOT 1: Multivariate Analysis (Stock vs. Velocity) ---
sns.scatterplot(ax=axes[0, 0], data=df, x='sales_velocity', y='current_stock', 
                hue='stockout_risk', style='stockout_risk', palette='coolwarm', s=120, alpha=0.8)
axes[0, 0].set_title('A. Class Separation: Inventory Dynamics', fontsize=15)

# --- PLOT 2: Correlation Matrix (Masked Triangle) ---
corr = df.select_dtypes(include=[np.number]).corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(ax=axes[0, 1], data=corr, mask=mask, annot=True, cmap='RdBu_r', center=0, fmt='.2f')
axes[0, 1].set_title('B. Feature Inter-Correlation Matrix', fontsize=15)

# --- PLOT 3: Kernel Density Estimate (KDE) for Lead Time ---
sns.kdeplot(ax=axes[1, 0], data=df, x='lead_time', hue='stockout_risk', fill=True, palette='viridis', bw_adjust=.5)
axes[1, 0].set_title('C. Probabilistic Lead Time Impact on Risk', fontsize=15)

# --- PLOT 4: Advanced Boxen Plot for Pricing ---
sns.boxenplot(ax=axes[1, 1], data=df, x='stockout_risk', y='price', palette='rocket')
axes[1, 1].set_title('D. Price Tier Distribution across Risk Categories', fontsize=15)

# Save high-res for GitHub
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
os.makedirs('data', exist_ok=True)
plt.savefig('data/advanced_diagnostic_dashboard.png', dpi=300)
print("SUCCESS: Advanced dashboard saved to 'data/advanced_diagnostic_dashboard.png'")
plt.show()