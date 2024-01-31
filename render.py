import time
import requests
import folium

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d

table = pq.read_table('./data.parquet')
table.to_pandas()

center = [40.641766, -73.780968]
mymap = folium.Map(location=center, zoom_start=5)

for i, j in table.iterrows():
    folium.Marker(location=[]).add_to(mymap)

mymap.save("map.html")