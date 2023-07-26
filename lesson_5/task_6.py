"""Написати функцію яка прибере з dict елементи із значеннями None:
  {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
  Повинно повернути {'first_color': 'Red', 'second_color': 'Green'} #
   * dict може бути довільним"""


def remove_none(d):
    return {i: v for i, v in d.items() if v is not None}


a = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
print(remove_none(a))