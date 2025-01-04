import requests
import time

API_URL = "https://api.telegram.org/bot"
BOT_TOKEN = "5452706659:AAH_hZchULI0cLGd4tZXS5S-P8_Bln2ji0k"
API_CAT_URL = "https://api.thecatapi.com/v1/images/search"
TEXT_ERROR = "Здесь должен быть котик"
MAX_COUNTER = 10

offset = -2
count = 0
cat_link: str
cat_response: requests.Response

while count < MAX_COUNTER:
    print("attempt = ", count)
    updates = requests.get(f"{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}").json()
    if updates["result"]:
        for result in updates["result"]:
            offset = result["update_id"]
            chat_id = result["message"]["from"]["id"]
            cat_response = requests.get(API_CAT_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0][
                    "url"
                ]  # распарсим JSON и вытащим ссылку на картинку
                requests.get(
                    f"{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}"
                )
            else:
                requests.get(
                    f"{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_ERROR}"
                )
    time.sleep(1)
    count += 1
