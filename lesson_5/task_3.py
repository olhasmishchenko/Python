"""Написати функцію яка поверне площу фігури: за замовчуванням
трикутника, опціонально квадрату. На вході 2 величини та параметр
 типу фігури."""


def calculate_square(figure, value1, value2):
    if figure == 'Трикутник':
        return 0,5 * value1 * value2
    elif figure == 'Квадрат':
        return value1 ** 2
    else:
        return None