"""** дод. Написати функцію `is_date`, що приймає 3 аргументи -
день, місяць і рік. Повернути `True`, якщо дата коректна (треба
враховувати число місяця. Наприклад 30.02 - дата не коректна,
так само 31.06 або 32.07 тощо), та `False` інакше.
(можна використовувати модуль datetime)"""


from datetime import datetime


def is_date(day, month, year):
    try:
        datetime.strptime(f"{day}/{month}/{year}", "%d/%m/%Y")
        return True
    except ValueError:
        return False
