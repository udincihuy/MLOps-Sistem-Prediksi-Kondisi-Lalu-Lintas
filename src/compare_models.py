print("=== Model Comparison ===")

old_rmse = 3.5
new_rmse = 2.8

print(f"Old RMSE : {old_rmse}")
print(f"New RMSE : {new_rmse}")

if new_rmse < old_rmse:
    print("PROMOTE TO PRODUCTION")
else:
    print("KEEP CURRENT MODEL")
