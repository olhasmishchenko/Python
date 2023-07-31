"""У додатку є json файл. Написати програму, яка прочитає його
та порахує загальну тривалість всіх треків в альбомі.
  Базовий кейс - поверне кількість секунд.
  * Дод. ускладнення повернути у вигляді рядка години:хвилини:
  секунди, прик. 0:41:39"""

import json
import datetime


def open_data():
    with open('acdc.json') as f:
        return json.load(f)


def total_duration(duration: dict) -> int:
    result = 0
    for track in data['tracks']:
        result += int(duration['duration'])
    return result


def seconds_to_datetime(result):
    hours = result // 3600
    minutes = (result % 3600) // 60
    seconds = result % 60

    time_in_format = datetime.time(hour=hours,
                                   minute=minutes,
                                   second=seconds).strftime('%H:%M:%S')
    return time_in_format


data = open_data()
total_second = total_duration(data)
print(total_second)
print(f'{seconds_to_datetime(data)}')






