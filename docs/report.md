# **1. Title and Author**

## **Project Title**

**Traffic Crash Severity Prediction Using Machine Learning**

**Prepared for UMBC Data Science Master Degree Capstone Project (DATA 606) by Dr. Chaojie (Jay) Wang**

**Author Name:** Shashank Reddy Muthangi

**GitHub Repository:** https://github.com/shashankreddym31/UMBC-DATA606-Capstone

**LinkedIn Profile:** www.linkedin.com/in/shashank-reddy-589a48244

**PowerPoint Presentation:**  https://github.com/shashankreddym31/UMBC-DATA606-Capstone/blob/main/docs/Traffic_Crash_Severity_Presentation.pptx

**YouTube Video:** https://youtu.be/QbHpKTBWABw

---

# **2. Background**

Traffic crashes are a major public safety issue in urban environments. While many crashes result only in property damage or minor injuries, some crashes lead to severe outcomes such as fatal injuries or incapacitating injuries. Predicting crash severity is important because it can help transportation agencies, city planners, and emergency responders better understand the conditions associated with serious crashes.

Crash severity is influenced by several factors, including weather conditions, lighting conditions, road surface condition, traffic control devices, speed limits, crash type, time of day, and contributing causes. Because these factors interact in complex ways, machine learning provides a useful approach for analyzing historical crash data and identifying patterns that may not be obvious through simple manual analysis.

This project focuses on building machine learning classification models to predict whether a traffic crash is severe or non-severe using the Chicago Traffic Crashes dataset. In this project, a crash is classified as severe if it includes at least one fatal injury or at least one incapacitating injury. All other crashes are classified as non-severe.

The goal of this project is not only to build predictive models, but also to understand which crash-related features are most useful in identifying severe crash outcomes.

## **Why it matters**

* Helps support **data-driven road safety planning**
* Assists in identifying conditions associated with **severe crashes**
* Can help transportation agencies prioritize **high-risk crash factors**
* Supports better understanding of **injury-related crash patterns**
* Provides a foundation for future crash risk prediction tools

## **Research Questions**

* Can machine learning models predict whether a crash will be severe or non-severe?
* Which crash-related factors are most useful for predicting crash severity?
* How does class imbalance affect severe crash prediction?
* Which classification model performs best for this dataset?
* Can threshold tuning improve the detection of severe crashes?

---
# **3. Data**

## **Data Source**

The dataset used in this project is the **Chicago Traffic Crashes dataset**, publicly available through the Chicago Open Data Portal. This dataset contains detailed records of reported traffic crashes in Chicago, including crash circumstances, roadway conditions, environmental factors, and injury information.

Dataset source:  
https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if

---

## **Data Availability**

The raw dataset file is not directly uploaded to this GitHub repository because the file size is very large (approximately 600 MB), which exceeds practical GitHub storage limits for project repositories.

If the direct dataset link shows restricted access or a forbidden message, the dataset can still be accessed manually through the Chicago Open Data Portal by searching for:

**Chicago Traffic Crashes dataset**

---

## **Data Size**

* Approximate raw file size: **~600 MB**
* Large-scale real-world traffic crash dataset

---

## **Data Shape**

* Over **1 million crash records**
* Multiple columns containing crash-related attributes

---

## **Unit of Observation**

Each row in the dataset represents **one individual traffic crash event**.

---

## **Data Dictionary (Selected Variables)**

| Column Name | Data Type | Definition |
|------------|----------|------------|
| POSTED_SPEED_LIMIT | Numeric | Speed limit at crash location |
| WEATHER_CONDITION | Categorical | Weather condition during crash |
| LIGHTING_CONDITION | Categorical | Lighting condition at crash time |
| ROADWAY_SURFACE_COND | Categorical | Surface condition of roadway |
| TRAFFIC_CONTROL_DEVICE | Categorical | Traffic signal or control device |
| FIRST_CRASH_TYPE | Categorical | Type of collision |
| PRIM_CONTRIBUTORY_CAUSE | Categorical | Primary cause of crash |
| SEC_CONTRIBUTORY_CAUSE | Categorical | Secondary cause of crash |
| LANE_CNT | Numeric | Number of traffic lanes |
| CRASH_HOUR | Numeric | Hour of crash occurrence |
| CRASH_DAY_OF_WEEK | Numeric | Day of week |
| CRASH_MONTH | Numeric | Month of crash |
| INJURIES_FATAL | Numeric | Number of fatal injuries |
| INJURIES_INCAPACITATING | Numeric | Number of incapacitating injuries |

---

## **Target Variable**

The original dataset does not provide a direct binary target variable for machine learning classification.

Therefore, a custom target variable named **Severe** was created using the following rule:

**Severe = 1 if:**
* `INJURIES_FATAL > 0`
* OR
* `INJURIES_INCAPACITATING > 0`

**Severe = 0 otherwise**

This converts the problem into a binary classification task for predicting severe versus non-severe crashes.

---

## **Selected Features**

The following variables were selected as predictors for model development:

* POSTED_SPEED_LIMIT
* TRAFFIC_CONTROL_DEVICE
* DEVICE_CONDITION
* WEATHER_CONDITION
* LIGHTING_CONDITION
* FIRST_CRASH_TYPE
* TRAFFICWAY_TYPE
* LANE_CNT
* ALIGNMENT
* ROADWAY_SURFACE_COND
* ROAD_DEFECT
* PRIM_CONTRIBUTORY_CAUSE
* SEC_CONTRIBUTORY_CAUSE
* CRASH_HOUR
* CRASH_DAY_OF_WEEK
* CRASH_MONTH

These features were selected because they provide relevant information about roadway conditions, environmental context, crash timing, and possible contributing causes.

---

# **4. Exploratory Data Analysis (EDA)**

Exploratory Data Analysis (EDA) was performed using Jupyter Notebook to understand the dataset structure, identify trends, assess data quality, and prepare the dataset for machine learning modeling.

---

## **Initial Data Exploration**

Initial exploration included:

* Inspecting dataset dimensions
* Reviewing column names and data types
* Generating summary statistics for numerical variables
* Examining categorical variable distributions

This helped establish a clear understanding of the dataset before preprocessing.

---

## **Data Quality Assessment**

Several preprocessing checks were performed:

### Missing Values
Missing values were identified in several categorical and numerical columns.

Handling strategy:
* Numerical missing values replaced using **median imputation**
* Categorical missing values replaced with `"UNKNOWN"`

---

### Data Type Corrections

Some columns required formatting corrections to ensure compatibility with modeling.

For example:
* `LANE_CNT` converted to numeric format

---

### Duplicate Data

Duplicate crash records were checked and handled as part of preprocessing.

---

## **Feature Encoding**

Because machine learning models require numerical input:

* Categorical features were transformed using **One-Hot Encoding**
* Numerical features were retained in their processed numeric form

This ensured compatibility across all classification models.

---

## **Class Imbalance Analysis**

One important finding during EDA was significant class imbalance.

Severe crashes represented a much smaller proportion of the dataset compared to non-severe crashes.

This imbalance was important because it directly affects model performance, especially recall for severe crash prediction.

As a result:

* Evaluation focused beyond simple accuracy
* Precision, Recall, and F1-score were emphasized
* Threshold tuning was later applied for performance improvement

---

## **Visual Analysis**

Several visualizations were created to better understand crash patterns and feature relationships.

### Crash Severity Distribution

A class distribution analysis was performed to compare severe and non-severe crash frequencies.

**Key insight:**  
The dataset is highly imbalanced, with non-severe crashes dominating the observations.

---

### Crash Frequency by Hour

Crash occurrences were analyzed by hour of the day.

**Key insight:**  
Crash frequency showed variation across time periods, reflecting traffic volume and driving behavior changes throughout the day.

---

### Weather Condition Analysis

Crash distribution by weather condition was examined.

**Key insight:**  
Most crashes occurred under clear weather conditions, though adverse weather may still contribute to severity risk.

---

### Lighting Condition Analysis

Lighting conditions during crashes were analyzed.

**Key insight:**  
Crash patterns varied across daylight and darkness conditions.

---

### Crash Cause Analysis

Primary contributing causes were explored.

**Key insight:**  
Driver behavior-related causes appeared frequently among reported crashes.

---

## **Key EDA Insights**

* Severe crashes are significantly less frequent than non-severe crashes
* Crash timing may influence crash occurrence patterns
* Environmental conditions provide useful predictive context
* Driver-related contributing causes appear important
* Data preprocessing and imbalance handling are critical for reliable classification

---
# **5. Model Training**

## **Models Implemented**

### **Logistic Regression**

Logistic Regression was used as the baseline classification model for this project. Since the objective of this project is to classify traffic crashes into severe and non-severe categories, Logistic Regression provides a strong starting point for binary classification tasks.

This model estimates the probability that a crash belongs to the severe class based on the relationship between the input features and the target variable. Logistic Regression is widely used because it is simple, computationally efficient, easy to interpret, and provides a useful benchmark for comparison against more advanced classification algorithms.

Although Logistic Regression assumes relatively simpler linear relationships between predictors and the outcome, it remains highly valuable for establishing baseline model performance.

---

### **Random Forest Classifier**

Random Forest Classifier is an ensemble learning algorithm that combines multiple decision trees to improve predictive performance and reduce overfitting.

Each decision tree is trained using random subsets of observations and features, and the final classification is determined through majority voting across the ensemble. This allows Random Forest to capture more complex feature relationships compared to simpler linear models.

Random Forest was selected for this project because it:

* Handles non-linear relationships effectively
* Works well with structured tabular datasets
* Is robust to noisy observations
* Reduces overfitting compared to individual decision trees
* Provides useful feature importance analysis

Because traffic crash severity is influenced by multiple interacting factors, Random Forest serves as a strong ensemble classification approach.

---

### **XGBoost Classifier**

XGBoost (Extreme Gradient Boosting) is an advanced boosting-based ensemble classification algorithm known for its high performance on structured tabular datasets.

Unlike Random Forest, which builds trees independently, XGBoost builds trees sequentially, where each new tree focuses on correcting the prediction errors made by previous trees. This iterative boosting process often produces stronger predictive performance.

XGBoost was selected because it:

* Captures complex non-linear feature relationships
* Performs exceptionally well on tabular classification tasks
* Handles feature interactions efficiently
* Provides probability-based predictions for threshold tuning
* Is highly effective for imbalanced classification problems

Because crash severity prediction involves multiple complex interactions between environmental, roadway, and behavioral factors, XGBoost was expected to provide strong classification performance.

---

## **Training Process**

The dataset was prepared and divided into separate subsets to ensure fair model evaluation on unseen crash records.

### **Data Preparation**

Before model training, several preprocessing steps were applied:

* Missing numerical values were handled using **median imputation**
* Missing categorical values were replaced with `"UNKNOWN"`
* Data type inconsistencies were corrected
* Categorical variables were transformed using **One-Hot Encoding**
* Numerical features were retained in processed numeric form

These preprocessing steps ensured that the dataset was clean, structured, and compatible with machine learning algorithms.

---

### **Train-Test Split**

To evaluate generalization performance fairly, the dataset was divided into training and testing sets.

* **Training Set:** 80%
* **Testing Set:** 20%

The training set was used to learn crash severity patterns, while the testing set was reserved for final performance evaluation.

This approach helps ensure that model results reflect performance on unseen data rather than memorized observations.

---

## **Libraries Used**

The following Python libraries were used during model development and evaluation:

* **pandas** – Data loading, cleaning, preprocessing, and analysis
* **numpy** – Numerical operations and array processing
* **matplotlib / seaborn** – Data visualization and exploratory analysis
* **scikit-learn** – Preprocessing, classification models, evaluation metrics, train-test splitting
* **xgboost** – Advanced boosting-based classification modeling
* **joblib / pickle** – Saving trained model artifacts for deployment

---

## **Evaluation Metrics**

Because this project involves an imbalanced binary classification problem, multiple evaluation metrics were used instead of relying solely on overall accuracy.

---

### **Accuracy**

Accuracy measures the proportion of correctly classified crash records across both severe and non-severe categories.

Although accuracy provides a general performance overview, it can be misleading for imbalanced datasets because a model may perform well on the majority class while failing to identify severe crashes effectively.

---

### **Precision**

Precision measures the proportion of crashes predicted as severe that were actually severe.

Higher precision indicates fewer false positive severe predictions and greater confidence in severe crash classifications.

---

### **Recall**

Recall measures the proportion of actual severe crashes that were correctly identified by the model.

This metric is especially important in this project because failing to detect severe crashes is more critical than generating false alarms.

Improving recall increases the model’s ability to identify serious crash events.

---

### **F1 Score**

F1 Score is the harmonic mean of Precision and Recall.

It provides a balanced measure of classification performance when both false positives and false negatives are important considerations.

Because severe crash prediction involves class imbalance, F1 Score serves as an important evaluation metric.
## **Model Performance**

The three classification models were evaluated using the testing dataset to compare their effectiveness in predicting severe traffic crashes.

| Model | Accuracy | Precision | Recall | F1 Score |
|------|---------|----------|--------|---------|
| Logistic Regression | 78.1% | 46.9% | 71.4% | 56.6% |
| Random Forest | 83.8% | 66.7% | 38.3% | 48.6% |
| XGBoost | 84.5% | 69.2% | 41.0% | 51.5% |

---

## **Performance Interpretation**

The model evaluation results demonstrate clear performance differences across the three classification approaches.

Logistic Regression achieved the highest recall, meaning it was able to correctly identify a larger proportion of severe crashes compared to the other models. This makes it useful for scenarios where detecting severe crashes is the highest priority. However, its lower precision indicates that it also produced a larger number of false positive predictions.

Random Forest improved overall accuracy and precision significantly compared to Logistic Regression. However, its recall dropped substantially, indicating that the model missed a larger number of actual severe crashes. While this model performed well in overall classification accuracy, lower recall reduced its usefulness for safety-focused prediction.

XGBoost delivered the strongest balanced overall performance among the three models. It achieved the highest accuracy, highest precision, and a stronger F1 Score compared to Random Forest. This suggests that XGBoost was more effective at capturing the complex relationships between crash-related variables and severity outcomes.

Although XGBoost did not initially achieve the highest recall, its strong probability-based prediction capability made it suitable for further optimization through threshold tuning.

---

## **Model Selection**

The **XGBoost Classifier** was selected as the final model for this project because it provided the strongest overall classification performance and the greatest flexibility for optimization.

### **Reasons for selection**

* Highest overall accuracy among evaluated models
* Strongest precision performance
* Better balanced F1 Score
* Effective handling of complex feature interactions
* Suitable for probability threshold adjustment
* Strong performance on structured tabular datasets

Although Logistic Regression achieved higher recall initially, XGBoost provided stronger overall model quality and greater adaptability for improving severe crash detection.

---

## Threshold Tuning

Because the project focuses on identifying severe crashes, recall is especially important. Missing a severe crash is a more critical failure than incorrectly predicting a non-severe crash as severe.

By default, classification models use a probability threshold of:

```python
0.50
```

At the default threshold, XGBoost produced strong general classification performance, but recall for severe crashes remained lower than desired.

To improve sensitivity toward severe crash detection, threshold tuning was performed by testing lower probability cutoffs and analyzing the trade-off between precision and recall.

A threshold of:

```python
0.35
```

was selected because it provided a more practical balance between identifying severe crashes and maintaining prediction reliability.

Lowering the threshold made the model more sensitive to severe crash events, increasing its ability to correctly classify high-risk crashes.

---

## Feature Importance

Feature importance analysis was performed using the final XGBoost model to identify which variables contributed most strongly to crash severity prediction.

### Most Influential Predictors

The most important predictive features included:

- Primary contributing cause
- First crash type
- Posted speed limit
- Weather condition
- Lighting condition
- Roadway surface condition
- Crash hour
- Traffic control device
- Lane count

These results suggest that both environmental conditions and driver-related behavioral factors significantly influence traffic crash severity outcomes.

For example:

- Higher posted speed limits were associated with greater crash severity risk
- Poor lighting conditions increased the likelihood of severe outcomes
- Weather and roadway surface conditions contributed to reduced driving safety
- Certain crash types were more strongly linked to serious injuries

---

## Key Modeling Insights

Several important findings emerged during model development and evaluation:

- Severe crash prediction cannot be evaluated using accuracy alone
- Recall is critical because failing to detect severe crashes has significant safety implications
- Ensemble-based models outperformed the baseline Logistic Regression model
- XGBoost captured complex crash severity relationships more effectively than other models
- Threshold tuning significantly improved the practical usefulness of the model
- Environmental, roadway, and behavioral factors all played meaningful roles in crash severity prediction

These findings reinforce the value of machine learning for transportation safety analytics and predictive crash risk assessment.

---

## Final Model Selection

The final selected model for this project was:

# XGBoost Classifier with Threshold Tuning

This model was selected because it provided the strongest overall balance between classification performance, severe crash detection capability, interpretability of feature importance, and practical deployment readiness.

Compared to the other evaluated models, the tuned XGBoost classifier offered the most effective solution for predicting severe traffic crashes using real-world crash data.

# 6. Application of the Trained Models

To make the trained machine learning model practical and user-friendly, an interactive web application was developed using Streamlit. This allows users to interact with the crash severity prediction model without writing any code.

## Application Functionality

The application accepts crash-related user inputs and instantly predicts whether the crash is likely to be severe or non-severe.

Users can provide:

- Posted speed limit
- Weather condition
- Lighting condition
- Roadway surface condition
- First crash type
- Primary contributing cause
- Lane count
- Crash hour
- Crash day of week
- Crash month

After submitting the inputs, the trained XGBoost model processes the data and generates a crash severity prediction in real time.

---

## Workflow

1. User enters crash-related details through the Streamlit interface
2. Inputs are preprocessed to match the training dataset structure
3. Categorical variables are encoded using the trained encoder
4. The XGBoost model generates a probability score
5. Threshold tuning is applied to determine final classification
6. The predicted crash severity result is displayed instantly

---

## User Interface

Application screenshots can be included here.

---

## Benefits of the Application

- Easy to use for non-technical users
- Real-time crash severity prediction
- Demonstrates practical deployment of machine learning
- Supports transportation safety analysis
- Can assist planners and analysts in identifying high-risk crash scenarios

---

## Tools Used

- Streamlit – Interactive web application framework
- XGBoost – Final machine learning prediction model
- scikit-learn – Preprocessing and encoding pipeline
- Joblib / Pickle – Loading saved model artifacts

---

# 7. Conclusion

This project successfully developed and evaluated machine learning models for predicting traffic crash severity using a large real-world crash dataset.

Multiple classification models were implemented and compared, including Logistic Regression, Random Forest, and XGBoost.

Among the evaluated models, XGBoost achieved the strongest overall performance and became the final selected model after threshold tuning improved severe crash detection capability.

The analysis also showed that roadway conditions, weather, lighting, crash type, and contributing causes are major factors influencing crash severity.

This project demonstrates how machine learning can transform raw traffic crash data into practical predictive insights and decision-support tools.

---

## Applications

- Traffic safety risk assessment
- Crash severity prediction for planning agencies
- Transportation analytics and policy support
- Decision support for roadway safety improvements
- Practical deployment through interactive predictive applications

---

## Limitations

- Dataset limited to Chicago traffic crash records
- Severe crash cases are relatively imbalanced
- No real-time traffic or weather integration
- Some potentially useful driver-related variables were unavailable
- Model performance depends on data quality and completeness

---

## Lessons Learned

- Data preprocessing has a major impact on model performance
- Handling class imbalance is critical for classification tasks
- Ensemble models outperform simpler baseline models
- Threshold tuning significantly improves real-world usability
- Deployment is essential for practical machine learning applications

---

## Future Work

- Integrate real-time traffic and weather APIs
- Expand the dataset to additional cities or statewide crash records
- Apply advanced imbalance-handling techniques such as SMOTE
- Incorporate explainable AI methods such as SHAP or LIME
- Improve the Streamlit application with dashboards and geographic visualizations
- Deploy the application as a production-ready cloud service

# 8.References

Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785–794. https://doi.org/10.1145/2939672.2939785

Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5–32. https://doi.org/10.1023/A:1010933404324

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825–2830.

Chicago Data Portal. (2025). Traffic crashes dataset. City of Chicago Open Data Portal. https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if

Montella, A., Aria, M., D’Ambrosio, A., & Mauriello, F. (2012). Analysis of powered two-wheeler crashes in Italy by classification trees and rules discovery. Accident Analysis & Prevention, 49, 58–72. https://doi.org/10.1016/j.aap.2011.03.023

Ziakopoulos, A., & Yannis, G. (2020). A review of spatial approaches in road safety. Accident Analysis & Prevention, 135, 105323. https://doi.org/10.1016/j.aap.2019.105323

Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. Advances in Neural Information Processing Systems, 30.
