# 🩺 Diabetes Prediction in Women of Reproductive Age  
### End-to-End Healthcare Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)
![Healthcare ML](https://img.shields.io/badge/Domain-Healthcare-red)
![Status](https://img.shields.io/badge/Status-Deployed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🔍 Why This Project Matters
Type 2 diabetes is increasingly prevalent among **women of reproductive age**, yet diagnosis often happens **too late**, after complications have already begun.

This project demonstrates how **machine learning can support early risk detection**, using routinely collected clinical data to flag potential diabetes cases before symptoms escalate.

> 🎯 **Business & Clinical Goal:**  
Enable early screening and decision support using an interpretable, deployable ML model.

---

## 📌 Project Summary (Recruiter Snapshot)
- **Problem:** Late detection of diabetes in women of reproductive age  
- **Solution:** Supervised machine learning classification model  
- **Model:** Support Vector Machine (SVM)  
- **Tech Stack:** Python, scikit-learn, pandas, SMOTE  
- **Deployment:** Model serialized and deployment-ready  
- **Focus:** Healthcare relevance, data quality, model reliability  

---

## 📊 Dataset Overview
Structured clinical dataset containing key predictors commonly used in diabetes screening.

### 🎯 Target Variable
- `Outcome`  
  - `0` → Non-Diabetic  
  - `1` → Diabetic  

### 🧾 Features
| Feature | Description |
|------|------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | Serum insulin |
| BMI | Body mass index |
| DiabetesPedigreeFunction | Genetic risk indicator |
| Age | Patient age |

---

## ⚙️ Tools & Technologies
- **Language:** Python  
- **Libraries:**  
  - Data Processing: pandas, numpy  
  - Visualization: matplotlib, seaborn  
  - Machine Learning: scikit-learn, imblearn (SMOTE)  
- **Environment:** Jupyter Notebook  
- **Model Persistence:** pickle  

---

## 🔄 Machine Learning Workflow

### 1️⃣ Exploratory Data Analysis
- Distribution analysis of clinical variables  
- Class imbalance identification  
- Statistical comparison of diabetic vs non-diabetic groups  

---

### 2️⃣ Data Preprocessing
- Replaced physiologically impossible zero values with median estimates  
- Train / validation / test split  
- Addressed class imbalance using **SMOTE**

✔ Ensures fair learning and improved minority-class prediction  

---

### 3️⃣ Model Development
- Algorithm: **Support Vector Machine (Linear Kernel)**  
- Trained on balanced dataset  
- Generated class predictions and probability scores  

---

### 4️⃣ Model Evaluation
Evaluation focused on **generalization and reliability**, not just accuracy:

- Training, validation, and test accuracy  
- Confusion Matrix  
- Precision, Recall, F1-score (Classification Report)  

✔ No significant overfitting observed  
✔ Balanced performance across classes  

---

## 📈 Results & Insights
- Consistent performance across data splits  
- Improved recall for diabetic class after SMOTE  
- Clear diagnostic insights using confusion matrix visualization  

📌 Interpretation-first evaluation, critical for healthcare ML systems.

---

## 🚀 Deployment Readiness
- Model serialized using `pickle`  
- Accepts real-time patient inputs  
- Easily deployable with **Streamlit or Flask**

### Example Input
```python
input_data = (5, 166, 72, 19, 175, 25.8, 0.587, 51)

Output

0 → Non-Diabetic

1 → Diabetic

🧠 Key Skills Demonstrated

✔ Healthcare data preprocessing
✔ Handling class imbalance (SMOTE)
✔ Model evaluation beyond accuracy
✔ ML pipeline design
✔ Deployment-ready modeling
✔ Responsible AI mindset

Future Enhancements

Hyperparameter tuning & model comparison

Feature importance & explainability (SHAP)

Web-based clinical screening tool

Expanded dataset & external validation

👩‍⚕️ About the Author

Healthcare Data Scientist & Machine Learning Engineer

I build end-to-end machine learning systems for healthcare problems — from data cleaning and modeling to evaluation and deployment — with a strong focus on accuracy, interpretability, and patient impact.

📬 Open to:

Entry-level / junior ML roles

Healthcare data science opportunities

Research & product collaborations
