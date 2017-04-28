import requests
import csv
from geopy.geocoders import Nominatim
geolocator = Nominatim()

inputfile = open('AMZ_FF.txt','r')
outputfile = csv.writer(open('AMZ_FF_GEO.txt','w'))

for row in inputfile:
	row = row.rstrip()
	location = geolocator.geocode(row)
	#print((location.address,location.latitude, location.longitude))
	newrow = [row,location.latitude,location.longitude]
	outputfile.writerow(newrow)
	

	
