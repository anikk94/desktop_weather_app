import weather
import tkinter as tk

import datetime

from PIL import Image, ImageTk

def update_clock():
    label_clock.config(text=f"{datetime.datetime.now().strftime('%H:%M:%S')}")
    root.after(1000, update_clock)

def update_weather():
    w.refresh_weather()
    label_temperature.config(text=f"Temp: {w.data['main']['temp']:7}\u00B0C")
    wind_kmph = w.data['wind']['speed'] * 3.6
    label_wind.config(text=f"Wind: {wind_kmph:.2f} km/h")
    refreshed_at = datetime.datetime.fromtimestamp(w.data['dt'])
    label_refreshed_at.config(text=f"Weather Data Timestamp: {refreshed_at}")

w = weather.Weather()

root = tk.Tk()
root.title("Weather App")

normal_font = ("Consolas", 30)
big_font = ("Consolas", 55)

# start at some size
root.geometry("800x480")
# full screen app
# root.attributes('-fullscreen', True)
# start maximized
# root.state('zoomed')
# use none of these to start compact

# Title Block
weather_app_image = Image.open("weather_logo.png")
resized_weather_app_image = weather_app_image.resize((100, 100))
tkweather_app_image = ImageTk.PhotoImage(resized_weather_app_image)


# App Content

# App Title Display
#   TODO: make the images toggle light and dark mode for the app
title_bar = tk.Frame(root)
# title_bar.configure(bg="teal") 
# title_bar.rowconfigure(1, weight=1)
title_bar.columnconfigure(1, weight=1)
title_bar.pack(fill="x", pady=(10, 10))
label_image = tk.Label(title_bar, image=tkweather_app_image)
# label_image.configure(bg="teal")
label_image.grid(row=0, column=0)
label_page_title = tk.Label(title_bar, text="Weather App", font=("Ariel", 55, "bold"))
label_page_title.grid(row=0, column=1)
label_image = tk.Label(title_bar, image=tkweather_app_image)
# label_image.configure(bg="teal")
label_image.grid(row=0, column=2)



# Calendar and Clock Block
'''
%d: Returns the day of the month, from 1 to 31.
%m: Returns the month of the year, from 1 to 12.
%Y: Returns the year in four-digit format (Year with century). like, 2021.
%y: Reurns year in two-digit format (year without century). like, 19, 20, 21
%A: Returns the full name of the weekday. Like, Monday, Tuesday
%a: Returns the short name of the weekday (First three character.). Like, Mon, Tue
%B: Returns the full name of the month. Like, June, March
%b: Returns the short name of the month (First three character.). Like, Mar, Jun
%H: Returns the hour. from 01 to 23.
%I: Returns the hour in 12-hours format. from 01 to 12.
%M: Returns the minute, from 00 to 59.
%S: Returns the second, from 00 to 59.
%f: Return the microseconds from 000000 to 999999
%p: Return time in AM/PM format
%c: Returns a locale’s appropriate date and time representation
%x: Returns a locale’s appropriate date representation
%X: Returns a locale’s appropriate time representation
%z: Return the UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
%Z: Return the Time zone name (empty string if the object is naive).
%j: Returns the day of the year from 01 to 366
%w: Returns weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
%U: Returns the week number of the year (Sunday as the first day of the week) from 00 to 53
%W: Returns the week number of the year (Monday as the first day of the week) from 00 to 53
'''
current_datetime = datetime.datetime.now()
day = current_datetime.strftime("%a")
date = current_datetime.strftime("%Y-%m-%d")

calendar_block = tk.Frame(root)
calendar_block.pack(fill="x")
calendar_block.columnconfigure(0, weight=1)
# calendar_block.configure(bg="red")
label_datetime = tk.Label(calendar_block, text=f"|  {day}  |  {date}  |", font=normal_font)
label_datetime.configure(bg="lightgreen")
label_datetime.grid(row=0, column=0, sticky="w")
# label_clock = tk.Label(calendar_block, text="HH:MM:SS", font=normal_font)
label_clock = tk.Label(calendar_block, text="HH:MM", font=normal_font)
label_clock.configure(bg="lightgreen")
label_clock.grid(row=0, column=1)


# Weather Information Block
info_block = tk.Frame(root)
info_block.pack(fill="both", padx=10, pady=10)
label_temperature = tk.Label(info_block, text=f"Temp: {w.data['main']['temp']:7}\u00B0C", font=big_font)
# label_temperature.configure(bg="red")
label_temperature.pack(fill="x")
wind_kmph = w.data['wind']['speed'] * 3.6
label_wind = tk.Label(info_block, text=f"Wind: {wind_kmph:.2f} km/h", font=big_font)
# label_wind.configure(bg="green")
label_wind.pack(fill="x")


# label_dev = tk.Label(root, text=w.data, wraplength=600)
# label_dev.pack()


# App Footer Section
# label_footer = tk.Label(root)
# label_footer.pack(pady=1, side="bottom")

refreshed_at = datetime.datetime.fromtimestamp(w.data['dt'])
label_refreshed_at = tk.Button(root, text=f"Weather Data Timestamp: {refreshed_at}", command=update_weather)
label_refreshed_at.pack(side="bottom", fill="x")

label_location = tk.Label(root, text=f"Location: {w.data['name']}", font=normal_font)
label_location.configure(bg="lightgreen")
label_location.pack(fill="x", side="bottom")




update_clock()
root.mainloop()
