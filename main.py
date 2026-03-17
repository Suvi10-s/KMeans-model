from fastapi import FastAPI
import joblib
from schema import Features

app=FastAPI()

model=joblib.load("KMeans.pkl")
scaler=joblib.load("scaler.pkl")

@app.get("/")
def home():
    return {"message":"customer segmentation"}

@app.post("/predict")
def prediction(features:Features):
    new_data=list(features.dict().values())
    data_scaled=scaler.transform([new_data])
    cluster = model.predict(data_scaled)
    return {"prediction":int(cluster[0])}