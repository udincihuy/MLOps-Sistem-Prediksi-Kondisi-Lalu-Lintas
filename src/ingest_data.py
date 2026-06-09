import yfinance as yf
import pandas as pd
import os

def ingest_data():
    
    data = yf.download("CL=F", period="2000d", interval="1d")


    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data.reset_index(inplace=True)

    filename = "data/raw/oil.csv"
    os.makedirs("data/raw", exist_ok=True)

    if os.path.exists(filename):
      
        existing = pd.read_csv(filename, parse_dates=["Date"])

       
        data = pd.concat([existing, data])
        
       
        data["Date"] = pd.to_datetime(data["Date"])
        data = data.drop_duplicates(subset=["Date"], keep="last")

    
    data = data.sort_values(by="Date")

    data.to_csv(filename, index=False)
    print(f"[INFO] Data berhasil diperbarui dan disimpan di {filename}")

if __name__ == "__main__":
    ingest_data()