import requests
import yaml

class Weather:
    def __init__(self):
        self.yaml_file = "key.yaml"

        with open(self.yaml_file, "r") as file:
            self.config = yaml.safe_load(file)

        self.api_url = "http://api.openweathermap.org/data/2.5/weather"
        self.api_key = self.config["api_key"]

        self.params = {
            "q": "Montgomery Village",
            "appid": self.api_key,
            "units": "metric",
        }
    
        self.data = self.get_weather()

    def get_weather(self):
        '''
        make a request for new weather data and return the result
        '''
        response = requests.get(self.api_url, params=self.params)

        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        else:
            print("error")
    
    def print_weather(self):
        '''
        print stored json weather data
        '''
        print(self.data)
    
    def refresh_weather(self):
        '''
        request for new weather data and store it
        '''
        self.data = self.get_weather()

if __name__ == "__main__":
    w = Weather()
    w.print_weather()


# Sample API JSON output
# {
#   "coord": {
#     "lon": -77.1953,
#     "lat": 39.1768
#   },
#   "weather": [
#     {
#       "id": 500,
#       "main": "Rain",
#       "description": "light rain",
#       "icon": "10n"
#     }
#   ],
#   "base": "stations",
#   "main": {
#     "temp": 0.92,
#     "feels_like": -1.46,
#     "temp_min": 0.29,
#     "temp_max": 1.59,
#     "pressure": 1022,
#     "humidity": 94,
#     "sea_level": 1022,
#     "grnd_level": 1004
#   },
#   "visibility": 8047,
#   "wind": {
#     "speed": 2.06,
#     "deg": 90
#   },
#   "rain": {
#     "1h": 0.76
#   },
#   "clouds": {
#     "all": 100
#   },
#   "dt": 1739411404,
#   "sys": {
#     "type": 1,
#     "id": 4182,
#     "country": "US",
#     "sunrise": 1739361837,
#     "sunset": 1739400135
#   },
#   "timezone": -18000,
#   "id": 4362743,
#   "name": "Montgomery Village",
#   "cod": 200
# }