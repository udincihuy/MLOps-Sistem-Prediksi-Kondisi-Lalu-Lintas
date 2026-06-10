import pandas as pd
import mlflow
import mlflow.sklearn

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

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

for n_estimators in [100, 200, 500]:
    for max_depth in [1, 3, 5]:
        for learning_rate in [0.01, 0.05, 0.1]:

            with mlflow.start_run():

                model = XGBRegressor(
                    n_estimators=n_estimators,
                    max_depth=max_depth,
                    learning_rate=learning_rate,
                    random_state=42
                )

                model.fit(X_train, y_train)

                y_pred = model.predict(X_test)

                rmse = mean_squared_error(
                    y_test,
                    y_pred
                ) ** 0.5

                mlflow.log_param(
                    "n_estimators",
                    n_estimators
                )

                mlflow.log_param(
                    "max_depth",
                    max_depth
                )

                mlflow.log_param(
                    "learning_rate",
                    learning_rate
                )

                mlflow.log_metric(
                    "rmse",
                    rmse
                )

                mlflow.sklearn.log_model(
                    sk_model=model,
                    artifact_path="model",
                    registered_model_name="harga_minyak_model"
                )

                print(
                    f"n_estimators={n_estimators}, "
                    f"max_depth={max_depth}, "
                    f"learning_rate={learning_rate}, "
                    f"RMSE={rmse:.4f}"
                )