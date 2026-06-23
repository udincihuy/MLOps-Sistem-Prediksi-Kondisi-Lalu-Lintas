import pandas as pd

def preprocess():
    file = "data/raw/oil.csv"

        data = pd.read_csv(file)

   
    data = data.dropna()
    data = data.drop_duplicates(subset=["Date"])

    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values(by="Date")

  
    data['lag1'] = data['Close'].shift(1)
    data['lag2'] = data['Close'].shift(2)
    data['ma3'] = data['Close'].rolling(3).mean()


    data['target'] = data['Close'].shift(-1)

    data = data.dropna()


    data = data[['Close', 'lag1', 'lag2', 'ma3', 'target']]

    data.to_csv("data/processed.csv", index=False)

    print("[INFO] Preprocessing selesai")

if __name__ == "__main__":
    preprocess()