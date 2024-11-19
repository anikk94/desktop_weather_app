import weather
import tkinter as tk

w = weather.Weather()

def update_weather():
    weather_info = w.get_weather()
    temp_label.config(text=f"Temperature: {weather_info['temperature']}°C")
    weather_label.config(text=f"Weather: {weather_info['description']}")

root = tk.Tk()
root.title("Weather App")

temp_label = tk.Label(root, text="Temperature: ")
temp_label.pack()

weather_label = tk.Label(root, text="Weather: ")
weather_label.pack()

update_button = tk.Button(root, text="Update Weather", command=update_weather)
update_button.pack()

root.mainloop()