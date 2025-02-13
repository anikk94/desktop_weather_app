#!/usr/bin/env python3
import weather
import tkinter as tk

import datetime

from PIL import Image, ImageTk

def simulate_periodic_key_press(key='<Return>'):
    root.event_generate(key)
    log_print("press <Return>")
    root.after(600000, simulate_periodic_key_press)

def log_print(msg):
    print(
        f"[{datetime.datetime.now().strftime('%Y-%m-%d - %H:%M:%S')}] {msg}"
    )

def update_datetime_and_clock():
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
    now = datetime.datetime.now()
    # day = now.strftime("%a")
    # date = now.strftime("%Y-%m-%d")
    label_datetime.config(
        text=f" {now.strftime('%a')} | {now.strftime('%Y-%m-%d')}")
    label_clock.config(text=f"{now.strftime('%H:%M:%S')} ")
    root.after(1000, update_datetime_and_clock)

def update_weather():
    log_print("update_weather()")
    w.refresh_weather()
    label_weather_symbol.config(image=weather_dict[w.data["weather"][0]["main"]])
    label_temperature.config(text=f"Temp: {w.data['main']['temp']:7}\u00B0C")
    wind_kmph = w.data['wind']['speed'] * 3.6
    label_wind.config(text=f"Wind: {wind_kmph:.2f} km/h")
    refreshed_at = datetime.datetime.fromtimestamp(w.data['dt'])
    label_refreshed_at.config(text=f"Weather Data Timestamp: {refreshed_at}")
    root.after(300000, update_weather)

# --------------------------------------------------------------------------- #
#                                    MAIN                                     #
# --------------------------------------------------------------------------- #
w = weather.Weather()

root = tk.Tk()
root.title("Weather App")

normal_font = ("Consolas", 30)
big_font = ("Consolas", 55)

# root.geometry("800x480") # start at a particular size
root.attributes('-fullscreen', True) # full screen app
# root.state('zoomed') # start maximized
# use none of these to start compact

# Title Block

# Load Image Resources
# --------------------
# app logo (explainer code)
icon_size = (80,80)
app_logo_raw = Image.open("weather_logo.png")
resized_app_logo = app_logo_raw.resize((100, 100))
tk_app_logo = ImageTk.PhotoImage(resized_app_logo)
# weather condition symbols
cloud_img=ImageTk.PhotoImage(Image.open("resources/cloud_85857.png").resize(icon_size))
moon_img=ImageTk.PhotoImage(Image.open("resources/moon_85908.png").resize(icon_size))
rain_img=ImageTk.PhotoImage(Image.open("resources/rain_85872.png").resize(icon_size))
snow_img=ImageTk.PhotoImage(Image.open("resources/snow_85899.png").resize(icon_size))
snowflake_img=ImageTk.PhotoImage(Image.open("resources/snowflake_85882.png").resize(icon_size))
storm_img=ImageTk.PhotoImage(Image.open("resources/storm_85835.png").resize(icon_size))
sun_img=ImageTk.PhotoImage(Image.open("resources/sun_85879.png").resize(icon_size))
suncloud_img=ImageTk.PhotoImage(Image.open("resources/suncloud_85840.png").resize(icon_size))
wind_img=ImageTk.PhotoImage(Image.open("resources/wave_85842.png").resize(icon_size))

weather_dict={
    "Thunderstorm":storm_img,
    "Drizzle":rain_img,
    "Rain":rain_img,
    "Snow":snow_img,
    "Atmosphere":wind_img,
    "Clear":sun_img,
    "Clouds":cloud_img,
}

# --------------------------------------------------------------------------- #
#                                App Content                                  #
# --------------------------------------------------------------------------- #
# App Title Display
# -----------------
# TODO: make the images toggle light and dark mode for the app
title_bar = tk.Frame(root)
# title_bar.configure(bg="teal") 
# title_bar.rowconfigure(1, weight=1)
title_bar.columnconfigure(1, weight=1)
title_bar.pack(fill="x", pady=(10, 10))
label_image = tk.Label(title_bar, image=tk_app_logo)
# label_image.configure(bg="teal")
label_image.grid(row=0, column=0)
label_page_title = tk.Label(title_bar, text="Weather", font=("Ariel", 55, "bold"))
label_page_title.grid(row=0, column=1)
label_image = tk.Label(title_bar, image=tk_app_logo)
# label_image.configure(bg="teal")
label_image.grid(row=0, column=2)

# Calendar and Clock Block
#-------------------------
calendar_block = tk.Frame(root)
calendar_block.configure(bg="lightgreen")
calendar_block.pack(fill="x")
calendar_block.columnconfigure(0, weight=1)
# calendar_block.configure(bg="red")
label_datetime = tk.Label(calendar_block, text=f" DDD | YYYY-MM-DD", font=normal_font)
label_datetime.configure(bg="lightgreen")
label_datetime.grid(row=0, column=0, sticky="w")
# label_clock = tk.Label(calendar_block, text="HH:MM:SS", font=normal_font)
label_clock = tk.Label(calendar_block, text="HH:MM:SS ", font=normal_font)
label_clock.configure(bg="lightgreen")
label_clock.grid(row=0, column=1)

# Weather Information Block
# -------------------------
placeholderS="---"
placeholderN=99

weather_section = tk.Frame(root)
weather_section.config(borderwidth=5, bg="green", relief="flat")
weather_section.pack(fill="both")
weather_section.columnconfigure(1,weight=1)


label_weather_symbol=tk.Label(weather_section,image=weather_dict["Clear"], width=200, height=200)
label_weather_symbol.config(bg="lightblue")
# label_weather_symbol.pack()
label_weather_symbol.grid(row=0,column=0)

weather_data_frame=tk.Frame(weather_section)
weather_data_frame.config(padx=10)
weather_data_frame.grid(row=0,column=1,sticky="nsew")

# label_temperature = tk.Label(weather_section, text=f"Temp: {w.data['main']['temp']:7}\u00B0C", font=big_font)
label_temperature = tk.Label(weather_data_frame, text=f"Temp: {placeholderS:7}\u00B0C", font=big_font)
# label_temperature.configure(bg="red")
# label_temperature.pack(fill="x")
label_temperature.grid(row=0,column=0,sticky="ew")
wind_kmph = w.data['wind']['speed'] * 3.6
# label_wind = tk.Label(weather_data_frame, text=f"Wind: {wind_kmph:.2f} km/h", font=big_font)
label_wind = tk.Label(weather_data_frame, text=f"Wind: {placeholderN:.2f} km/h", font=big_font)
# label_wind.configure(bg="green")
# label_wind.pack(fill="x")
label_wind.grid(row=1,column=0,sticky="ew")
label_spacer = tk.Label(weather_data_frame)
label_spacer.grid(row=2,column=0,sticky="nsew")

# label_dev = tk.Label(root, text=w.data, wraplength=600)
# label_dev.pack()

# Forecast Section
# ----------------
forecast_section=tk.Frame(root)
# forecast_section.config(borderwidth=1,bg="cornsilk")
forecast_section.pack(fill="x")
label_placeholder1=tk.Label(forecast_section,text="forecast section placeholder")
label_placeholder1.pack()

# App Footer Section
# ------------------
# label_footer = tk.Label(root)
# label_footer.pack(pady=1, side="bottom")

refreshed_at = datetime.datetime.fromtimestamp(w.data['dt'])
label_refreshed_at = tk.Button(root, text=f"Weather Data Timestamp: {refreshed_at}", command=update_weather)
label_refreshed_at.pack(side="bottom", fill="x")

label_location = tk.Label(root, text=f"Location: {w.data['name']}", font=normal_font)
label_location.configure(bg="lightgreen")
label_location.pack(fill="x", side="bottom")

# --------------------------------------------------------------------------- #
#                             Configure Events                                #
# --------------------------------------------------------------------------- #
update_datetime_and_clock()
simulate_periodic_key_press()
update_weather()
root.mainloop()

