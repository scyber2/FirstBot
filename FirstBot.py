# API
# Automation updates
import requests
import time

api_url: str = 'https://api.telegram.org/bot'
token_bot: str = '5971044342:AAGvKEGRBjv8aBpUypGBFbckjXN25oYWQhU'
photo: str = 'https://api.thecatapi.com/v1/images/search'
error_text: str = 'Здесь должна была быть картинка с котиком :('
max_counter: int = 20

offset: int = -2
counter: int = 0
chat_id: int

while counter < max_counter:
    print(f'attempt = {counter}')
    updates = requests.get(f'{api_url}{token_bot}/getUpdates?offset={offset + 1}').json()
    print(updates)

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(photo)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{api_url}{token_bot}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{api_url}{token_bot}/sendMessage&chat_id={chat_id}&text={error_text}')

    time.sleep(1)
    counter += 1
