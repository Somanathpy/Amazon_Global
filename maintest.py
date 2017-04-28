import folium
import pandas as pd
import sys
sys.stdin.encoding
#df = pandas.read_csv("AMZ_SD_Places.txt",encoding='utf-16')
df = pd.read_csv("AMZ_CS_GEO.txt", delimiter=",", encoding='latin1')
#print (df.to_string())
map = folium.Map(location=[45.372,-121.697],zoom_start=3,tiles='openstreetmap')

cs = folium.FeatureGroup(name="AMZ CS")
for lat,lon,name in zip(df['LATITUDE'],df['LONGITUDE'],df['NAME']):
	cs.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='red')))
map.add_child(cs)
	
df = pd.read_csv("AMZ_FF_GEO.txt", delimiter=",", encoding='latin1')
#print (df.to_string())
#map = folium.Map(location=[df['LATITUDE'].mean(),df['LONGITUDE'].mean()],zoom_start=3,tiles='openstreetmap')
ff = folium.FeatureGroup(name="AMZ FF")
for lat,lon,name in zip(df['LATITUDE'],df['LONGITUDE'],df['NAME']):
	ff.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='green')))

map.add_child(ff)
df = pd.read_csv("AMZ_SD_GEO.txt", delimiter=",", encoding='latin1')
#print (df.to_string())
#map = folium.Map(location=[df['LATITUDE'].mean(),df['LONGITUDE'].mean()],zoom_start=3,tiles='openstreetmap')
sd = folium.FeatureGroup(name="AMZ SD")
for lat,lon,name in zip(df['LATITUDE'],df['LONGITUDE'],df['NAME']):
	sd.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='orange')))
map.add_child(sd)
map.add_child(folium.LayerControl())

map.save(outfile='main.html')
