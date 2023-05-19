import requests
import time

api_url = 'https://api.telegram.org/bot'
bot_token = '5971044342:AAGvKEGRBjv8aBpUypGBFbckjXN25oYWQhU'
counter = 0
offset = -2


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{api_url}{bot_token}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    time.sleep(3)
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')