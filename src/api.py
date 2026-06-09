from fastapi import FastAPI
import pandas as pd
import mlflow

app = FastAPI()

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_registry_uri("sqlite:///mlflow.db")

model = mlflow.pyfunc.load_model(
    "models:/harga_minyak_model/Production"
)

@app.get("/")
def home():
    return {"message": "Oil Price Prediction API"}

@app.post("/predict")
def predict():

    data = pd.DataFrame({
        "lag1": [100],
        "lag2": [98],
        "ma3": [99]
    })

    prediction = model.predict(data)

    return {
        "prediction": float(prediction[0])
    }