import time
import requests
import csv
import folium

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import matplotlib.pyplot as plt

center = [40.641766, -73.780968]
mymap = folium.Map(location=center, zoom_start=5)

with open('data.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        folium.Marker(location=[row[0], row[1]]).add_to(mymap)

mymap.save("map.html")