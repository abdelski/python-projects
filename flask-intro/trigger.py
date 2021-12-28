import requests
endpoint = 'http://127.0.0.1:8000/box'

r = requests.post(endpoint, json={})
print(r.text)