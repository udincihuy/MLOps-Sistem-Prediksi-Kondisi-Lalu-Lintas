import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Prediksi_Harga_Minyak")


def train_model(alpha):
    data = pd.read_csv("data/processed.csv")

    
    X = data[['lag1', 'lag2', 'ma3']]

 
    y = data['target']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )


    model = Ridge(alpha=alpha)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred) ** 0.5
    THRESHOLD = 10

    if rmse > THRESHOLD:
        raise ValueError(f"RMSE terlalu besar: {rmse}")
    return model, rmse


if __name__ == "__main__":
    for alpha in [0.001, 0.01, 0.1, 1.0, 10.0]:

        with mlflow.start_run():
            model, rmse = train_model(alpha)

            mlflow.log_param("alpha", alpha)
            mlflow.log_metric("rmse", rmse)

            mlflow.sklearn.log_model(model, "model")

            print(f"Run alpha={alpha}, RMSE={rmse}")