import tkinter as tk 
import requests
from tkinter import messagebox
from PIL import Image,ImageTk 
import ttkbootstrap

# the api from open weather

def get_weather(city):
    API_key="0d9a41652b4e798eb120e24cca445fad"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

# error

    if res.status_code == 404:
        messagebox.showerror("Error", "city not found")
        return None
    
#the temp and city 
     
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)


#the temp results 

def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    icon_url,  temperature, description, city, country = result
    loacation_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon 

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")


# geometry and title

root = ttkbootstrap.Window(themename="morph")
root.title("weather app")
root.geometry("400x400") 


city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)


search_button= ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

loacation_label = tk.Label(root, font="Helvetica, 25")
loacation_label.pack(pady=20)

icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()