import geocoder
myloc = geocoder.ip('me')
print('your vehicle is at:')
a=myloc.latlng
#print(myloc.latlng)

