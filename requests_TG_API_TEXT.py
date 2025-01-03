import requests
import time

API_URL = "https://api.telegram.org/bot"
BOT_TOKEN = "5452706659:AAH_hZchULI0cLGd4tZXS5S-P8_Bln2ji0k"
TEXT = "Ура! Работает!"
MAX_COUNTER = 10

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:
    print("attempt = ", counter)  # чтобы видеть пока живет код
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(
                f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}'
            )
    time.sleep(1)
    counter += 1
