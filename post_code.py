import requests
import sys

data = {
    "license_id":"setw42354",
    "fingerprint_id":"2432235",
    "suspended":0
}

with requests.Session() as r:
    r.post('http://localhost:3000/data', data=data, headers={'Connection':'close'})
    r.close()