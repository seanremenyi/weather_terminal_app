import json
import requests


url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"Sydney"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "fa98bed2d4mshbf19405106ccc0bp14c91djsn9fe248ea1d29"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

respons = json.load(response.text)

print(respons)
# converted_json = json.loads(str(response))
# print(converted_json)

