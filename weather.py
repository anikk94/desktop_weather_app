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