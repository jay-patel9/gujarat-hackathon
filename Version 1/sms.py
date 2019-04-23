import requests
from geo import a
b = str(a[0])
c = str(a[1])
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=Your Vehicle is in trouble at "+b+","+c+"&language=english&route=p&numbers=9924346348"
headers = {
'authorization': "Z1cndXOzVu6QLlxI8PAvmRpksWwN3FUohK4YSqGT2J7Cyr5HBtin68NrKcbjwS9fGYhmOLIsBRplFo5z",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
#print(response.text)

ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
print(my_ip)

geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()
print("Latitute",geo_data['latitude'])
print("Longitude",geo_data["longitude"])
print(geo_data)
