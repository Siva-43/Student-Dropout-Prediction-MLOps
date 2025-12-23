from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# Load model
with open("app/model/model.pkl", "rb") as f:
    model = pickle.load(f)

# Load features
with open("app/model/features.pkl", "rb") as f:
    FEATURES = pickle.load(f)

@app.get("/")
def health():
    return {"status": "API running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    df = df[FEATURES]

    pred = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]

    return {
        "dropout_risk": int(pred),
        "probability": float(proba)
    }
