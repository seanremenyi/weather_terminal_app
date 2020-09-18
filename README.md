# Terminal Weather APP

This is a terminal weather application that I have created that consumes an API.

### __Purpose__

The purpose of this application is to give the user current weather conditions for the city he lives in (these include current meteorological conditions, temperature, wind speed, and time of sunset).

### __Target Audience__

Developers and other versed in using terminal applications who would like to know the weather outside. Possibly wanting to know the conditions if they can go outside for a break.

### __Outside Resources__

This application consumes the OpenWeather API which can be found at 
https://openweathermap.org/

This application requires an API key which can be obtained at https://openweathermap.org/price under the free tier.

### __Set Up__

This application uses python3.8 and some python3.8modules as well as getting an API key from OpenWeather

##### For the App,

1. Create a directory to clone the git repo into
2. Clone git repo
3. If not running python 3.8, run the following bash commands
    1. `sudo apt update`
    2. `sudo apt install python3.8`
4. Create a virtual enviornment
    1. `sudo apt-get install python3-pip`
    2. `sudo apt-get install python3-venv`
    3. `python3 -m venv venv`
5. Install the modules in requirements.txt

##### For the API Key,

1. Obtain a key from https://openweathermap.org/price
2. Set up an enviorment variable with the following command
    `export API_KEY = {API-Key}`

### __Running the APP__

The application can be ran by using the following bash command

`python3.8 weather.py`

From here the app will ask you for the city you are looking for. 

The Application expects the format of the first letter of the city capitalized followed by a comma and then followed by the 2-letter country code. For example

`Melbourne,Au`

If there is any 400 or 500 status code error, the application will ask you to re-input your city.

List of cities are available on the OpenWeather website


# Hope you enjoy!














