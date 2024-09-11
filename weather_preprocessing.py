import requests
from geopy.geocoders import Nominatim
import json
import datetime
from urllib.parse import quote_plus

api_weather = "77ef480b640d917eb7d4f19215b30430"

def process_address(location):
    api_yandex = "a783a53e-16a2-4164-ad19-20832f60c1f1"
    encoded_location = quote_plus(location)

    geocode_url = f"https://geocode-maps.yandex.ru/1.x/?apikey={api_yandex}&geocode={encoded_location}&format=json"

    response = requests.get(geocode_url)
    data = response.json()
    pos = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    lon, lat = map(float, pos.split())

    req = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_weather}&units=metric"

    response = requests.get(req)
    data1 = response.json()

    with open("data.json", "w", encoding="UTF-8") as file:
        json.dump(data1, file, ensure_ascii=False, indent=1)
    
    print("Данные успешно сохранены в файл data.json")

def json_parsing():
    with open("data.json", encoding="UTF-8") as file:
        data = json.load(file)
    
    punkt = data["name"]
    weather = data["weather"][0]
    maintemp = data["main"]
    weter = data["wind"]

    sunrise_timestamp = int(data["sys"]["sunrise"])
    sunset_timestamp = int(data["sys"]["sunset"])

    sunrise_time = datetime.datetime.fromtimestamp(sunrise_timestamp, tz=datetime.timezone.utc)
    timevosh = f"Время восхода солнца: {sunrise_time.strftime('%H:%M:%S')}"

    sunset_time = datetime.datetime.fromtimestamp(sunset_timestamp, tz=datetime.timezone.utc)
    timezakat = f"Время заката солнца: {sunset_time.strftime('%H:%M:%S')}"

    message = (
        f"Погода в населенном пункте {punkt}:\n"
        f"Температура: {int(maintemp['temp'])}°С\n"
        f"Ощущается как: {int(maintemp['feels_like'])}°С\n"
        f"Состояние погоды: {weather['main']}\n"
        f"Скорость ветра: {int(weter['speed'])} м/с"
    )
    return message

