import requests

from Config import Config


def fetch_weather():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={Config.CITY}&appid={Config.API_KEY}"

    try:
        response = requests.get(URL)
        data = response.json()
        return data
    except:
        print("Błąd")

result = fetch_weather()
print(result)
