# 📊 Content Monetization Modeler

## 🚀 Project Overview
This project predicts **YouTube Ad Revenue** for individual videos using regression models.  
It also includes a **Streamlit web application** for interactive predictions and analytics.

## 🎯 Problem Statement
As creators depend on ad revenue, predicting future earnings is crucial for:
- **Content Strategy Optimization**
- **Revenue Forecasting**
- **Creator Support Tools**
- **Ad Campaign Planning**

## 🛠️ Skills & Tools
- Python, Pandas, Scikit-learn
- Exploratory Data Analysis (EDA)
- Regression Models (Linear, Desicion tree,gradient boost, Random Forest, XGBoost)
- Feature Engineering & Preprocessing
- Data Visualization
- Streamlit App Deployment

## 📂 Dataset
- **Name**: YouTube Monetization Modeler  
- **Format**: CSV (~122,000 rows)  
- **Target Variable**: `ad_revenue_usd`  
- **Features**: views, likes, comments, watch time, video length, subscribers, category, device, country, etc.  

## 🔎 Approach
1. Dataset exploration & cleaning (handling missing values, duplicates, encoding).
2. Feature Engineering (e.g., Engagement Rate = (likes + comments)/views).
3. Train 5 regression models & compare performance.
4. Evaluate with R², RMSE, MAE.
5. Build **Streamlit App** for predictions & insights.

## 📈 Results
- Cleaned dataset ready for analysis.
- Regression model to predict YouTube Ad Revenue.
- Streamlit app with:
  - Revenue prediction from user input.
  - Visual analytics & model insights.




