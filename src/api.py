from fastapi import FastAPI
import pandas as pd
import yfinance as yf
import mlflow

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

mlflow.set_tracking_uri("sqlite:///mlflow.db")

model = mlflow.pyfunc.load_model(
    "models:/harga_minyak_model@production"
)


@app.get("/")
def home():
    return {
        "message": "Oil Price Prediction API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict():

    data = yf.download(
        "CL=F",
        period="5d",
        progress=False
    )

    if data.empty:
        return {
            "error": "Failed to fetch data from Yahoo Finance"
        }

    close = data["Close"]

    lag1 = float(close.iloc[-1])
    lag2 = float(close.iloc[-2])
    ma3 = float(close.tail(3).mean())

    X = pd.DataFrame({
        "lag1": [lag1],
        "lag2": [lag2],
        "ma3": [ma3]
    })

    prediction = model.predict(X)

    return {
    
        "prediction": float(prediction[0])
    }