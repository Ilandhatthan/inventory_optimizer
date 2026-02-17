📦 **Project: Inventory Optimizer**
This is an end-to-end data pipeline that handles everything from SQL database engineering to multi-model machine learning and Seaborn analytics.

🚀 **Key Features**
Database Power: Manages a relational schema with over 12,000 transaction rows.

Data Cleaning: Uses Pandas to fix missing prices and filter out negative stock errors.

Multi-Model ML: Compares Logistic Regression, Random Forest, and Linear Regression to find the best fit. 

Advanced Visuals: High-level Seaborn dashboard with heatmaps and feature analysis.

📂 **System Architecture**
To rebuild the project, run these scripts in this exact order:

src/1_generate_db.py: 
Builds the SQL database with 12k+ rows. 🏗️

src/2_clean_data.py: 
Cleans the uncleaned dataset using Python/Pandas. ✨

src/3_train_model.py: 
Trains multiple models and prints detailed metric reports. 📈

src/4_visualize_results.py: 
Generates the Seaborn diagnostic dashboard. 🎨

📊 **Machine Learning Evaluation**
We don't just guess; we compare models to see which one "hits" the hardest:

**Model                   Purpose                         Strength**
Logistic Regression     Baseline Risk Classification    Fast & Reliable
Random Forest           Advanced Pattern Detection      High Accuracy
Linear Regression       Sales Velocity Forecasting      Precise Predictions

📉 **Visual Insights (Seaborn)**
The final dashboard in your data/ folder includes:

Correlation Heatmap: Shows how sales speed and lead times drive stockout risk. 🔥

Feature Importance: Proves which variables are the real "bosses" in your model. 🎯