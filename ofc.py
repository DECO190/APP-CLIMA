import tkinter as tk
import requests
from time import sleep
LARG = 600
ALTU = 500
# 7a62227eb7ea6eaece1590216aa296da
def erro():
    return 'LOCAL NÃO ENCONTRADO'
def formata(climapo):
    name = climapo['name']
    desc = climapo['weather'][0]['description']
    temp = climapo['main']['temp'] - 273
    temp2 = round(temp,2)
    if temp2 > 15 and temp2 < 24:
        background_label1 = tk.Label(label, image = background1)
        background_label1.place(relx = 0.41, rely = 0.62, relwidth = 0.2 , relheight = 0.2)
    if temp2 > 24:
        background_label2 = tk.Label(label, image = background2)
        background_label2.place(relx = 0.4, rely = 0.6, relwidth = 0.2 , relheight = 0.25)
    if temp2 < 15:
        background_label3 = tk.Label(label, image = background3)
        background_label3.place(relx = 0.4, rely = 0.6, relwidth = 0.2 , relheight = 0.25)
    return str(name) + '\n ' + str(desc) + '\n' + str(temp2) + ' °C'


def get_weather(city):
    try:
        weatherkey = '7a62227eb7ea6eaece1590216aa296da'
        url='https://api.openweathermap.org/data/2.5/weather'
        params= {'APPID': weatherkey, 'q': city, 'units': 'Celsius'}
        response= requests.get(url, params= params)
        climapo= response.json()

        label['text']  = formata(climapo)
    except:
        label['text'] = erro()



root = tk.Tk()

root.title('Clima')

background1 = tk.PhotoImage(file = 'nublado.png')
background2 = tk.PhotoImage(file = 'hot.png')
background3 = tk.PhotoImage(file = 'cold.png')

canvas = tk.Canvas(root, height = ALTU, width = LARG) 
canvas.pack()

background = tk.PhotoImage(file = 'background.png')
background_label = tk.Label(root, image = background)
background_label.place(x = 0, y = 0, relwidth = 1 , relheight = 1)


frame = tk.Frame(root, bg= '#00CED1', bd = 5)
frame.place(relwidth= 0.75, relx = 0.5,rely = 0.1, relheight= 0.1, anchor = 'n')


entry = tk.Entry(frame, font = 40)
entry.place(relwidth = 0.65, relheight = 1 )


bttn = tk.Button(frame, text = "VERIFICAR" , font =40 ,  command= lambda: get_weather(entry.get()))
bttn.place(relx = 0.7, rely = 0, relwidth = 0.3, relheight = 1)


lower_frame = tk.Frame(root, bg = '#00CED1', bd = 10)
lower_frame.place(relx = 0.12 , rely = 0.25,relwidth= 0.76, relheight= 0.6)


label = tk.Label(lower_frame, bg = '#f0f0f0', font = 40)
label.place(relwidth = 1, relheight= 1)


root.mainloop()