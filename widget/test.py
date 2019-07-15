import requests
from requests import Session

s=requests.session()
r = s.post('http://127.0.0.1:5000/login', data={'username': 'ivan'})
print(r.text)
re = requests.get('http://127.0.0.1:5000/')
print(re.text)
req = s.get('http://127.0.0.1:5000/')
print(req.text)
