# API
import requests

path_api = 'https://api.telegram.org/bot5971044342:AAGvKEGRBjv8aBpUypGBFbckjXN25oYWQhU/sendMessage?chat_id=1993510301' \
           '&text=Привет, Артём!'
res = requests.get(path_api)
print(res.text if res.status_code == 200 else f'ERROR, your status_code now: {res.status_code}')