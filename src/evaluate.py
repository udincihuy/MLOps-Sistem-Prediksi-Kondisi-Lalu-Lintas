import pandas as pd
import mlflow

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


mlflow.set_tracking_uri("sqlite:///mlflow.db")


def evaluate():

    data = pd.read_csv("data/processed.csv")

    X = data[["lag1", "lag2", "ma3"]]
    y = data["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        shuffle=False
    )

    model = mlflow.pyfunc.load_model(
        "models:/harga_minyak_model@production"
    )

    y_pred = model.predict(X_test)

    rmse = mean_squared_error(
        y_test,
        y_pred
    ) ** 0.5

    print("=== EVALUATION RESULT ===")
    print(f"RMSE : {rmse:.4f}")


if __name__ == "__main__":
    evaluate()