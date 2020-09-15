import json
import requests
import datetime, pytz
import os

class Weather():
    
    def __init__(self, data):
        self.data=data

    def get_weather(self):
        self.weather= self.data["weather"][0]["description"]
        
    def get_temp(self):
        self.temp = self.data["main"]["temp"] - 270
    
    def get_wind(self):
        self.wind = self.data["wind"]["speed"]*3.6
    
    def get_sunset(self):
        timestamp = datetime.datetime.fromtimestamp(self.data["sys"]["sunset"])
        conv_timestamp=timestamp.astimezone(pytz.timezone("Australia/Melbourne"))
        self.sunset = conv_timestamp.strftime('%H:%M:%S')
        
    def get_city(self):
        self.city = f"{self.data['name']}, {self.data['sys']['country']}"

    def display_weather(self):
        print(f"""\nCurrently in {self.city}
        
        Weather outside is {self.weather}
        The temperature is {self.temp} degrees celcius
        The winds blowing at {self.wind} km/h
        Sunset's at {self.sunset}
        """)
        
    
def get_response():
    city = input(f"\nWhat city would you like the weather for? (Format: Melbourne,AU)\n")
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city.capitalize()}&appid={os.getenv('API_KEY')}")
    json_text = json.loads(response.text)
    if json_text['cod'] == 200:
            return json_text
    get_response()

main = Weather(get_response())
    
main.get_weather()
main.get_temp()
main.get_city()
main.get_sunset()
main.get_wind()
main.display_weather()


