import json
import requests
import datetime, pytz

class Weather():
    def __init__(self, weather, temp, sunset):
        self.weather = weather
        self.temp = temp
        self.sunset = sunset
    pass


response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Melbourne,au&appid=20427f6992caf7e1315b81df74c57fc9")
json = json.loads(response.text)

api_weather= json["weather"][0]["description"]
api_temp = json["main"]["temp"] - 270
api_wind = json["wind"]["speed"]
timestamp = datetime.datetime.fromtimestamp(json["sys"]["sunrise"])
conv_timestamp=timestamp.astimezone(pytz.timezone("Australia/Melbourne"))
api_sunset = conv_timestamp.strftime('%H:%M:%S')

print(f"\nOutside is {api_wind}")

