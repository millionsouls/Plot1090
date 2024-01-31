
import time

import requests
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

url = 'https://localhost:8080/data.json'
lat = [1]
lon = [1]
alt = [1]
tim = [1]

def genParquet():
    df = pd.DataFrame({'lat': lat,
                       'lon': lon,
                       'alt': alt,
                       'tim': tim,
                       })
    table = pa.Table.from_pandas(df)
    pq.write_table(table, './data.parquet')


while True:
    try:
        raw = requests.get(url)
        raw.raise_for_status

        data = raw.json()

        for x in data:
            if x.flight:
                lat.append(x.lat)
                lon.append(x.lon)
                alt.append(x.altitude)
                tim.append(int(time.time()))
    except requests.exceptions.RequestException as e:
        genParquet()
        raise SystemExit(e)
    
    time.sleep(1)