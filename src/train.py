import pandas as pd
import mlflow.sklearn

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

data = pd.read_csv("data/processed.csv")

X = data[["lag1", "lag2", "ma3"]]
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    shuffle=False
)

model = mlflow.sklearn.load_model(
    "best_model"
)

y_pred = model.predict(X_test)

rmse = mean_squared_error(
    y_test,
    y_pred
) ** 0.5

print("RMSE :", rmse)