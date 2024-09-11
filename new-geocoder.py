import requests
from urllib.parse import quote_plus
api = "api"
location = "Москва"
encoded_location = quote_plus(location)

geocode_url = f"https://geocode-maps.yandex.ru/1.x/?apikey={api}&geocode={encoded_location}&format=json"

response = requests.get(geocode_url)
data = response.json()

try:
    pos = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    lon, lat = map(float, pos.split())
except (IndexError, KeyError, ValueError) as e:
    print(f"Ошибка при получении координат: {e}")

print(lon, lat)