"""Написати функцію `is_prime`, що приймає 1 аргумент -
 число від 0 до 1000, і повертає `True`, якщо воно просте, і `False`
 - інакше."""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num) - 1):
        if num % i == 0:
            return False
    return True


