import time
import requests
import json

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

url = "http://localhost:8080/data.json"
lat = []
lon = []
alt = []
tim = []

def genParquet():
    df = pd.DataFrame({'lat': lat,
                       'lon': lon,
                       'alt': alt,
                       'tim': tim,
                       })
    table = pa.Table.from_pandas(df)
    pq.write_table(table, './data.parquet')


try: 
    while True:
        try:
            raw = requests.get(url, timeout=10, verify=False)
            data = raw.json()

            for x in data:
                print(x)
                if x.get('lat') != 0 and x.get('lon') != 0:
                    lat.append(x.get('lat'))
                    lon.append(x.get('lon'))
                    alt.append(x.get('altitude'))
                    tim.append(int(time.time()))
            
            genParquet()
        except requests.exceptions.RequestException as e:
            genParquet()
            raise SystemExit(e)
        
        time.sleep(1)
except KeyboardInterrupt:
    genParquet()
    print("terminated")