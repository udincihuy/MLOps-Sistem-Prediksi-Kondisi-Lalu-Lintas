import pandas as pd
import mlflow
import mlflow.sklearn

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Prediksi_Harga_Minyak")

data = pd.read_csv("data/processed.csv")

X = data[["lag1", "lag2", "ma3"]]
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    shuffle=False
)

n_estimators = 500
max_depth = 3
learning_rate = 0.1

with mlflow.start_run():

    model = XGBRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        learning_rate=learning_rate,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    rmse = root_mean_squared_error(
        y_test,
        y_pred
    )

    mlflow.log_params({
        "n_estimators": n_estimators,
        "max_depth": max_depth,
        "learning_rate": learning_rate
    })

    mlflow.log_metric(
        "rmse",
        rmse
    )

    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        registered_model_name="harga_minyak_model"
    )

    print("=== TRAINING SELESAI ===")
    print(f"RMSE : {rmse:.4f}")