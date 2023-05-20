import requests
import time

api_url = 'https://api.telegram.org/bot'

with open('ideas_for_bot.txt', encoding='utf-8') as file:
    bot_token = ''.join(list(file.readline())[-47:]).strip()

counter = 0
offset = -2
timeout: int = 10


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{api_url}{bot_token}/getUpdates?offset={offset + 1}&timeout={timeout}').json()
    print(updates)

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')
