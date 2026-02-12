# 1. Title and Author

### **Project Title**

**Traffic Crash Severity Prediction Using Machine Learning**

Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang

**Author Name:**  
Shashank Reddy Muthangi  

**GitHub Repository Link:**  
https://github.com/shashankreddym31/UMBC-DATA606-Capstone  

**LinkedIn Profile Link:**  
[To be added]

**PowerPoint Presentation Link:**  
[To be added after presentation is created]

**YouTube Video Link:**  
[To be added after project demo video is recorded]

---

# 2. Background

### What is it about?

This project focuses on analyzing traffic crash data and building a machine learning classification model to predict whether a crash will result in severe injuries.

A crash will be defined as severe if it involves:

- At least one fatal injury  
- At least one incapacitating injury  

The main goals of this project are:

1. To understand patterns associated with severe crashes.  
2. To build predictive models that classify crashes as severe or non-severe based on available features.  

---

### Why does it matter?

Traffic crashes are a major public safety issue in urban environments. Severe crashes can result in:

- Loss of life  
- Long-term disabilities  
- Increased healthcare costs  
- Economic and infrastructure impacts  

By identifying key factors associated with severe crashes, this project may help:

- Improve road safety awareness  
- Support data-driven safety planning  
- Provide insights for policymakers and city planners  

This project uses real-world crash data to develop predictive and analytical insights.

---

### Research Questions

1. Can crash severity be predicted using roadway, environmental, and temporal features?  
2. Which factors most strongly influence crash severity?  
3. How do different machine learning models compare in classifying severe crashes?  
4. How does class imbalance affect model performance?  

---

# 3. Data

To answer the research questions, a real-world traffic crash dataset is used in this project.

---

## Dataset – Chicago Traffic Crashes Dataset

### Data Source

The dataset used in this project is the **Chicago Traffic Crashes dataset**, publicly available through the Chicago Open Data Portal.

---

### Purpose of This Dataset

This dataset is used for:

- Binary classification (Severe vs Non-Severe)  
- Identifying contributing factors to crash severity  
- Comparing different machine learning models  

---

### Data Size

- Large-scale dataset (over 1 million records)  
- Format: CSV  

---

### Data Shape

- Number of rows: Over 1,000,000 crash records  
- Number of columns: Multiple features describing crash conditions and injury details  

---

### Time Period

The dataset contains crash records from multiple recent years.

---

### What Does Each Row Represent?

Each row in this dataset represents:

 **One individual traffic crash event**

---

## Data Dictionary (Selected Variables)

| Column Name | Data Type | Definition | Potential Values |
|-------------|----------|------------|-----------------|
| POSTED_SPEED_LIMIT | Integer | Speed limit at crash location | Numeric values |
| WEATHER_CONDITION | String | Weather at time of crash | Clear, Rain, Snow, etc. |
| LIGHTING_CONDITION | String | Lighting condition | Daylight, Darkness, etc. |
| ROADWAY_SURFACE_COND | String | Road surface condition | Dry, Wet, Snow, etc. |
| FIRST_CRASH_TYPE | String | Type of collision | Rear-end, Angle, etc. |
| PRIM_CONTRIBUTORY_CAUSE | String | Primary cause of crash | Speeding, Distracted Driving, etc. |
| LANE_CNT | Numeric | Number of lanes | Numeric values |
| CRASH_HOUR | Integer | Hour of crash (0–23) | 0–23 |
| CRASH_DAY_OF_WEEK | Integer | Day of week | 1–7 |
| CRASH_MONTH | Integer | Month of crash | 1–12 |
| INJURIES_FATAL | Integer | Number of fatal injuries | Numeric values |
| INJURIES_INCAPACITATING | Integer | Number of incapacitating injuries | Numeric values |

---

### Target Variable for Machine Learning

The dataset does not directly contain a binary severity label.

Therefore, a new variable will be created:

**Severe = 1 if:**

- INJURIES_FATAL > 0  
OR  
- INJURIES_INCAPACITATING > 0  

**Severe = 0 otherwise.**

This derived variable will be used as the **target/label variable** for classification.

---

### Features / Predictors for ML Models

The following columns may be selected as input features:

- POSTED_SPEED_LIMIT  
- WEATHER_CONDITION  
- LIGHTING_CONDITION  
- ROADWAY_SURFACE_COND  
- FIRST_CRASH_TYPE  
- PRIM_CONTRIBUTORY_CAUSE  
- LANE_CNT  
- CRASH_HOUR  
- CRASH_DAY_OF_WEEK  
- CRASH_MONTH  

These features will be used to predict the binary target variable **Severe**.

---

# Data Usage Strategy

The dataset will be used for:

| Task | Purpose |
|------|---------|
| Data cleaning and preprocessing | Handle missing values and prepare features |
| Exploratory Data Analysis | Understand distribution and class imbalance |
| Model training | Train classification models |
| Model evaluation | Compare performance metrics |

Special attention will be given to handling class imbalance since severe crashes are relatively rare compared to non-severe crashes.

---

# Summary

In this project:

- The Chicago Traffic Crashes dataset will be used for classification.  
- A derived binary variable called **Severe** will serve as the target.  
- Machine learning models such as Logistic Regression, Random Forest, and XGBoost will be explored.  
- Model performance will be evaluated using appropriate classification metrics.  

This structured approach provides a strong foundation for developing predictive insights into traffic crash severity.
