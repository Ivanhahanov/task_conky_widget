import requests

tasks = requests.get('http://127.0.0.1:5000').json()
for task in tasks:
	task = '${color ff0000}' + task + '${color}'
	print(task)
