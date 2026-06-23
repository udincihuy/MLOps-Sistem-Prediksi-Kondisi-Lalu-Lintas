import subprocess

print("=== RETRAINING STARTED ===")

subprocess.run(
    ["python", "src/train.py"],
    check=True
)

print("=== RETRAINING FINISHED ===")
