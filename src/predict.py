import mlflow
import pandas as pd

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_registry_uri("sqlite:///mlflow.db")

# Load model Production
model = mlflow.pyfunc.load_model(
    "models:/harga_minyak_model/Production"
)

# Ambil data terbaru
data = pd.read_csv("data/processed.csv")

# Ambil baris terakhir
latest = data.tail(1)

# Ambil fitur
X = latest[['lag1', 'lag2', 'ma3']]

# Prediksi
pred = model.predict(X)

print("Prediksi harga minyak berikutnya:", pred[0])