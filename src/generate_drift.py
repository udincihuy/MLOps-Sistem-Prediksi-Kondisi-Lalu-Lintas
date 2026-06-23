import pandas as pd

df = pd.read_csv("data/processed.csv")

# Simulasi perubahan distribusi data
df["target"] = df["target"] * 1.3

df.to_csv("data/new_data.csv", index=False)

print("Data drift berhasil dibuat")
