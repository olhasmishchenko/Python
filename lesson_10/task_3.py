"""Написати функцію яка зрушить отриманий список
на N елементів вправо або вліво, аргументи,
що приймаються - список і натуральне число
(якщо негативне зрушуємо вліво, позитивне - вправо)."""


def shift_list(some_list, n):
    if n > 0 or n < 0:
        return some_list[-n:] + some_list[:-n]
    else:
        return some_list


print(shift_list([1, 2, 3, 4, 5], 3))
print(shift_list([1, 2, 3, 4, 5], -3))