import requests

url = 'http://maps.googleapis.com/maps/api/geocode/json'
myaddress = 'NewYork'
mysensor = 'false'
payload = {'address':myaddress, 'sensor':mysensor}
r = requests.get(url, params=payload)

json = r.json()
lat = json['results'][0]['geometry']['location']['lat']
lng = json['results'][0]['geometry']['location']['lng']

print(lat,lng)