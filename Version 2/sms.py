import requests
from geo import a
b = str(a[0])
c = str(a[1])
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
print(my_ip)

geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()
lat = geo_data['latitude']
lon = geo_data["longitude"]
print("Latitute",)
print("Longitude",)
print(geo_data)

url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=Your Vehicle is in trouble at "+lat+","+lon+"&language=english&route=p&numbers=8160954987"
headers = {
'authorization': "Xs70Irjz9cn8qGtBfQpR3xVZLY5TlgkKWmFMuA1HyJNw2Uae4iWQa2G74nct8OEZ6v1bLYzkmqhFV5Bi",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
#print(response.text)


