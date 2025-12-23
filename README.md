# 🎓 Student Dropout Risk Prediction

An end-to-end Machine Learning project that predicts whether a student is at risk of dropping out of college using academic, attendance, and demographic data.

---

## 🚀 Project Overview

Student dropout is a major challenge for educational institutions. This project builds a production-ready ML system that:

- Trains a classification model to predict dropout risk
- Exposes predictions through a FastAPI REST API
- Packages everything using Docker for easy deployment

---

## 🧠 Machine Learning Pipeline

1. Data preprocessing (handling missing values, encoding)
2. Model training using tree-based ML models
3. Model serialization using Pickle
4. REST API creation with FastAPI
5. Containerization using Docker

---

## 🏗️ Project Structure

```text
Student_Dropout_Risk_Prediction/

├── app/
│   ├── main.py
│   └── model/
│       ├── model.pkl
│       └── features.pkl
├── model.ipynb
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore

⚙️ How to Run Locally

1️⃣ Build Docker Image
      docker build -t dropout-api .

2️⃣ Run Docker Container
      docker run -p 8000:8000 dropout-api
3️⃣ Test the API

     Open: http://localhost:8000/docs

📊 Example Output

{
  "dropout_risk": 1,
  "probability": 0.82
}

🛠️ Tech Stack

    Python

    Pandas, Scikit-learn, XGBoost

    FastAPI

Docker

🎯 Use Cases

   Early identification of at-risk students

   Targeted academic or financial interventions

   Improving student retention rates

📌 Future Improvements

   Model explainability (SHAP)

   MLflow experiment tracking

   Cloud deployment (AWS)

   CI/CD integration
