import requests
import pandas as pd
import os
import time

API_KEY = "RNQvEhetDURiITSlTCO3C0f9M1IbjUtD"

url = "https://www.mapquestapi.com/directions/v2/route"

routes = [
    ("New York, NY", "Washington, DC"),
    ("Los Angeles, CA", "San Diego, CA"),
    ("Chicago, IL", "Detroit, MI"),
    ("Dallas, TX", "Houston, TX"),
    ("San Francisco, CA", "San Jose, CA"),
    ("Boston, MA", "Philadelphia, PA"),
    ("Seattle, WA", "Portland, OR"),
    ("Miami, FL", "Orlando, FL"),
    ("Atlanta, GA", "Charlotte, NC"),
    ("Denver, CO", "Salt Lake City, UT")
]

results = []

for start, end in routes:

    params = {
        "key": API_KEY,
        "from": start,
        "to": end
    }

    response = requests.get(url, params=params)
    data = response.json()

    route = data["route"]

    distance = route["distance"]
    time_normal = route["time"]
    realtime = route["realTime"]

    ratio = realtime / time_normal

    if ratio < 1.1:
        condition = "lancar"
    elif ratio < 1.3:
        condition = "padat"
    else:
        condition = "macet"

    results.append({
        "from": start,
        "to": end,
        "distance_km": distance,
        "time_seconds": time_normal,
        "realTime_seconds": realtime,
        "traffic_condition": condition
    })

    time.sleep(1) 

df = pd.DataFrame(results)

os.makedirs("data/raw", exist_ok=True)

df.to_csv("data/raw/traffic_raw.csv", index=False)

print("Data berhasil disimpan dengan", len(df), "data")