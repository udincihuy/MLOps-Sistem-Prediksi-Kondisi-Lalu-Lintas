import pandas as pd

old_df = pd.read_csv("data/processed.csv")
new_df = pd.read_csv("data/new_data.csv")

old_mean = old_df["target"].mean()
new_mean = new_df["target"].mean()

drift_score = abs(new_mean - old_mean) / old_mean

print(f"Old Mean : {old_mean:.4f}")
print(f"New Mean : {new_mean:.4f}")
print(f"Drift Score : {drift_score:.4f}")

if drift_score > 0.2:
    print("RETRAIN")
else:
    print("NO RETRAIN")