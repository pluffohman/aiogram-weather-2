import json
import datetime

with open("data.json") as file:
    data = json.load(file)


weather = data["weather"][0]
print(weather)

maintemp = data["main"]
print(maintemp)

weter = data["wind"]
print(weter)

sunrise_timestamp = int(data["sys"]["sunrise"])
sunset_timestamp = int(data["sys"]["sunset"])

sunrise_time = datetime.datetime.fromtimestamp(sunrise_timestamp, tz=datetime.timezone.utc)
timevosh = f"Время восхода солнца: {sunrise_time.strftime('%H:%M:%S')}"

try:
    print(timevosh)
except DeprecationWarning:
    print(timevosh)

sunset_time = datetime.datetime.fromtimestamp(sunset_timestamp, tz=datetime.timezone.utc)
timezakat = f"Время заката солнца: {sunset_time.strftime('%H:%M:%S')}"

try:
    print(timezakat)
except DeprecationWarning:
    print(timevosh)

