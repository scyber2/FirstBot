# API
import requests

url_api = 'http://numbersapi.com/43'
response = requests.get(url_api)
print(response.text if response.status_code == 200 else response.status_code)