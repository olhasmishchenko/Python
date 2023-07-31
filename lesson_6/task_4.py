"""Написати функцію, яка повертає поточний час. І обернути
її у декоратор який відрахує 3 секунди."""

import datetime
import time


def delay_decorator(func):
    def wrapper():
        time.sleep(3)
        return func()
    return wrapper


@delay_decorator
def get_current_time():
    return datetime.datetime.now()


print(get_current_time())