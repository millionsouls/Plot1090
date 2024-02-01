import csv
import folium

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import matplotlib.pyplot as plt

center = [40.641766, -73.780968]
mymap = folium.Map(location=center, zoom_start=5)

fig = plt.figure()
ax = plt.axes(projection='3d')
lat = []
lon = []
alt = []

with open('data.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        lat.append(row[0])
        lon.append(row[1])
        alt.append(row[2])
        folium.Marker(location=[row[0], row[1]]).add_to(mymap)

ax.grid()
ax.plot(lat,lon,alt, marker='o', markersize=5)

mymap.save("map.html")
plt.show()