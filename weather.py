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
    
    def get_weather(self):
        response = requests.get(self.api_url, params=self.params)

        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        else:
            print("error")
    def print_weather(self):
        print(self.get_weather())
    

if __name__ == "__main__":
    w = Weather()
    w.print_weather()