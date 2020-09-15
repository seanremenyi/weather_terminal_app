import json
import requests
import datetime, pytz
import os

class Weather():
    def __init__(self, weather, temp, wind, sunset):
        self.weather = weather
        self.temp = temp
        self.wind = wind
        self.sunset = sunset
    
    def weather_display(self):
        return f"""
        
Today in Melbourne
Today's weather is {self.weather}
The temp outside is {self.temp} degrees celcius
The winds blowing at {self.wind} km/h
Sunset's at {self.sunset}

...get out there while that suns still out"""
        
    


response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=Melbourne,au&appid=20427f6992caf7e1315b81df74c57fc9")
json = json.loads(response.text)

api_weather= json["weather"][0]["description"]
api_temp = json["main"]["temp"] - 270
api_wind = json["wind"]["speed"]*3.6
timestamp = datetime.datetime.fromtimestamp(json["sys"]["sunset"])
conv_timestamp=timestamp.astimezone(pytz.timezone("Australia/Melbourne"))
api_sunset = conv_timestamp.strftime('%H:%M:%S')

todays_weather = Weather(api_weather, api_temp, api_wind, api_sunset)


print(todays_weather.weather_display())

