import requests
import csv

inputfile = open('places.txt','r')
#outputfile = csv.writer(open('geocoded-placelist.txt','w'))

for row in inputfile:
  row = row.rstrip()
  url = 'http://maps.googleapis.com/maps/api/geocode/json'
  mysensor = 'false'
  payload = {'address':row, 'sensor':mysensor}
  r = requests.get(url, params=payload)
  json = r.json()
  #print(json[results])
  lat = json['results'][0]['geometry']['location']['lat']
  lng = json['results'][0]['geometry']['location']['lng']
  print(lat,lng)
  #newrow = [row,lat,lng]
  #outputfile.writerow(newrow)