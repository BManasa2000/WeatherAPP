import tkinter as tk
from PIL import ImageTk,Image
import requests
from tkinter import font

#Current weather- api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = f"City: {name}\nConditions: {desc}\nTemparature(°C): {temp}"

    except:
        final_str = "There was a problem retrieving that information"

    return final_str

def get_weather(city):
    weather_key='******'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID': weather_key,'q': city,'units': 'metric'}
    response = requests.get(url,params=params)
    weather= response.json()

    formatted_weather=format_response(weather)
    label['text']=formatted_weather
    #text.delete(1.0,"end")
    #text.insert(1.0,formatted_weather)
    #msg['text']=formatted_weather

#every app we build with tkinter has a root
#we place everything in this root window
root= tk.Tk()
root.title("CurrentWeatherChecker")
root.resizable(False,False)


#we are using canvas as a placeholder to give initial screen size
canvas = tk.Canvas(root, height= 500, width= 700)
canvas.pack()
canvas.update()
HEIGHT = canvas.winfo_height()
WIDTH = canvas.winfo_width()

#setting the background image
image=Image.open("landscape2.jpg")
image=image.resize((WIDTH,HEIGHT))
#width, height = image.size
background_image= ImageTk.PhotoImage(image)
background_label= tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame= tk.Frame(root,bg="#ffe085",bd=3) #we make root the parent of it
frame.place(relx=0.025, rely=0.1, relwidth=0.45, relheight=0.1)

entry= tk.Entry(frame, font=("Courier",15))
entry.place(relwidth=0.65, relheight=1) #default relx=0,rely=0
entry.focus()

button = tk.Button(frame, text="Get weather", font=("Courier",11), command=lambda: get_weather(entry.get()))
button.place(relx=0.655, relheight=1, relwidth=0.345)

lower_frame = tk.Frame(root, bg="#ffe085", bd=3)
lower_frame.place(relx=0.025,rely=0.25,relwidth=0.45,relheight=0.3)

#msg=tk.Message(lower_frame,font=("Courier",11), anchor='nw', justify="left", bd=2)
#msg.place(relwidth=1, relheight=1)

#text= tk.Text(lower_frame, font=("Courier",13),height=10, bd=4)
#text.place(relwidth=1, relheight=1)

label= tk.Label(lower_frame, font=("Courier",13),anchor='nw', justify="left", bd=4, wraplength=300)
label.place(relwidth=1, relheight=1)

#to run the application
root.mainloop()