"""Отримати прогноз погоди для Одеси на наступні 5 днів
та записати у файл з ім'ям поточної дати"""

import requests
import datetime

city = "Odessa"
cnt = 5
units = "metric"
APPID = "f9ada9efec6a3934dad5f30068fdcbb8"
URL = (f'http://api.openweathermap.org/data/2.5/forecast/daily')

response = requests.get(URL).json()

forecast = []

for i in response["list_1"]:
    date = datetime.datetime.fromtimestamp(i["dt"])
    date_form = date.strftime("%d-%m-%Y")
    temp_day = i["temp"]["day"]
    temp_night = i["temp"]["night"]
    forecast.append((date_form, temp_day,temp_night))

file_name = f'{date_form}-{city}-{cnt}-weather.txt'

with open(file_name) as file:
    file.write("Дата Температура День Ночь")
    for forecast in forecast:
        date, temp_day, temp_night = forecast
        file.write(f'{date} {temp_day} {temp_night}')