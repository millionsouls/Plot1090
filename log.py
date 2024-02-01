import time
import requests
import json
import csv

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

url = "http://localhost:8080/data.json"
lat = []
lon = []
alt = []
tim = []

try: 
    with open ('data.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')

        while True:
            try:
                raw = requests.get(url, timeout=60, verify=False)
                data = raw.json()

                for x in data:
                    print(x)
                    if x.get('lat') != 0 and x.get('lon') != 0:
                        writer.writerow(x.get('lat'), x.get('lon'), x.get('altitude'), int(time.time()))
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
        
            time.sleep(1)
except KeyboardInterrupt:
    print("terminated")