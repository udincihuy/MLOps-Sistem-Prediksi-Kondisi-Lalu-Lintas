from fastapi import FastAPI
import pandas as pd
import yfinance as yf
import mlflow
from prometheus_fastapi_instrumentator import Instrumentator
app = FastAPI()
Instrumentator().instrument(app).expose(app)
model = mlflow.pyfunc.load_model(
    "best_model"
)


@app.get("/")
def home():
    return {
        "message": "Oil Price Prediction API"
    }


@app.post("/predict")
def predict():

    data = yf.download(
        "CL=F",
        period="5d",
        progress=False
    )

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