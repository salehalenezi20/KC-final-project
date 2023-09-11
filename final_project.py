import tkinter as tk 
import requests
from tkinter import messagebox
from PIL import Image,ImageTk 
import ttkbootstrap

# the api from open weather

def get_weather(city):
    API_k="0d9a41652b4e798eb120e24cca445fad"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_k}"
    resp = requests.get(url)

# error

    if resp.status_code == 404:
        messagebox.showerror("Error", "city not found")
        return None
    
#the temp and city 
     
    weather = resp.json()
    icon_id = weather['weather'][0]['icon']
    temp = weather['main']['temp'] - 273.15
    des = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temp, des, city, country)


#the temp results 

def search():
    city = city_ent.get()
    result = get_weather(city)
    if result is None:
        return
    icon_url,  temp, des, city, country = result
    loacation_1.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_lab.configure(image=icon)
    icon_lab.image = icon 

    temperature_lab.configure(text=f"Temperature: {temp:.2f}°C")
    description_1.configure(text=f"Description: {des}")


# geometry and title

root = ttkbootstrap.Window(themename="morph")
root.title("weather app")
root.geometry("400x400") 


city_ent = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_ent.pack(pady=10)


search = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search.pack(pady=10)

loacation_1 = tk.Label(root, font="Helvetica, 25")
loacation_1.pack(pady=20)

icon_lab = tk.Label(root)
icon_lab.pack()

temperature_lab = tk.Label(root, font="Helvetica, 20")
temperature_lab.pack()

description_1 = tk.Label(root, font="Helvetica, 20")
description_1.pack()

root.mainloop()