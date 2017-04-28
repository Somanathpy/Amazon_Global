import folium
import pandas as pd
import sys
sys.stdin.encoding
#df = pandas.read_csv("AMZ_SD_Places.txt",encoding='utf-16')
df = pd.read_csv("AMZ_CS_GEO.txt", delimiter=",", encoding='latin1')
#print (df.to_string())
map = folium.Map(location=[45.372,-121.697],zoom_start=3,tiles='openstreetmap')
for lat,lon,name in zip(df['LATITUDE'],df['LONGITUDE'],df['NAME']):
	map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='green')))

map.save(outfile='test2.html')