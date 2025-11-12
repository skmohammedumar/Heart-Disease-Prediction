# ❤️ Heart Disease Prediction Web App (Multi-Model ML Deployment)

A Flask-based web application that predicts whether a person is likely to have heart disease based on 13 medical input parameters.
This app integrates 9 machine learning models trained on the classic Heart Disease dataset and allows users to test predictions instantly.
---

## 🧠 Project Overview

This project is a **Heart Disease Prediction Web Application** that uses **9 classification algorithms** to predict whether a person is likely to have heart disease based on key medical attributes such as age, cholesterol, blood pressure, and more.

Users can input their data manually and choose any of the ML models to compare predictions instantly through the web interface.

---

## ⚙️ Tech Stack

- **Python 3.x**
- **Flask** (for backend deployment)
- **Scikit-learn**, **XGBoost**, **Numpy**, **Pandas**
- **HTML / CSS** (for frontend)
- **Pickle** (for model serialization)
- **Git & GitHub** (for version control)

---

## 🤖 Machine Learning Models Used

1. 🧩 K-Nearest Neighbors (KNN)  
2. 📈 Logistic Regression  
3. 📊 Naive Bayes  
4. 🌳 Decision Tree  
5. 🌲 Random Forest  
6. ⚡ AdaBoost  
7. 🚀 Gradient Boosting  
8. 💥 XGBoost  
9. 💡 Support Vector Machine (SVM)

All models are pre-trained and stored in a single pickle file (`all_models.pkl`) for easy loading and deployment.

---

## 🩺 Input Features

| Feature | Description |
|----------|--------------|
| **age** | Age of the person |
| **sex** | 1 = Male, 0 = Female |
| **cp** | Chest pain type |
| **trestbps** | Resting blood pressure |
| **chol** | Serum cholesterol (mg/dl) |
| **fbs** | Fasting blood sugar (>120 mg/dl) |
| **restecg** | Resting electrocardiographic results |
| **thalach** | Maximum heart rate achieved |
| **exang** | Exercise induced angina |
| **oldpeak** | ST depression induced by exercise |
| **slope** | Slope of peak exercise ST segment |
| **ca** | Number of major vessels (0–3) colored by fluoroscopy |
| **thal** | Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect) |

---

## 🧩 Folder Structure

heart-disease-multi-model-app/
│
ML_deployment/
│
├── app.py
├── all_models.pkl
├── requirements.txt 
├── templates/
│   └── index.html

⚙️ How to Run Locally
Step 1: Clone the repository
git clone https://github.com/<your-username>/heart-disease-prediction-app.git
cd heart-disease-prediction-app

Step 2: Install dependencies
pip install -r requirements.txt

Step 3: Run the Flask app
python app.py

Step 4: Open in browser
Go to:
👉 http://127.0.0.1:5000


🧪 Example Input
Feature	Value
Age	63
Sex	1
CP	1
Trestbps	150
Chol	260
FBS	1
Restecg	0
Thalach	112
Exang	1
Oldpeak	3.5
Slope	0
CA	2
Thal	2

✅ Expected Output: Heart Disease Detected

📦 Requirements
flask
numpy
pandas
scikit-learn==1.7.2
xgboost
gunicorn

