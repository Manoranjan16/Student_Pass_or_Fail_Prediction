# Student Pass-Fail Prediction

## Project Overview

This project predicts whether a student will **Pass** or **Fail** based on academic and personal factors using Machine Learning.

## Features

* Data preprocessing
* Label Encoding for categorical features
* StandardScaler for feature scaling
* Logistic Regression model
* Model serialization using Joblib
* User input-based prediction system

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

## Dataset Features

* Study Hours
* Attendance
* Past Score
* Internet Access
* Pass/Fail (Target Variable)

## Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Encoding
5. Train-Test Split
6. Feature Scaling using StandardScaler
7. Model Training using Logistic Regression
8. Model Evaluation
9. Save Model using Joblib
10. Predict Student Performance

## Model Performance

* Accuracy: 100%
* Precision: 100%
* Recall: 100%
* F1-Score: 100%

Note: The dataset used for testing was small. Performance may vary with larger datasets.

## Installation

```bash
pip install pandas numpy scikit-learn joblib
```

## Run the Project

```bash
python app.py
```

## Example Input

```text
Study Hours: 5
Attendance: 85
Past Score: 78
Internet Access: Yes
```

## Example Output

```text
Student will Pass
```

## Saved Files

```text
student_model.pkl
scaler.pkl
```

## Author

Manoranjan Behera
Machine Learning Enthusiast
