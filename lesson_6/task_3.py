"""Дано перелік значень. Повернути словник, де кожен ключ -
це індекс листа, а значення листа – це значення ключа:"""

def list_to_dict(list_test):
    return {i: list_test[i] for i in range(len(list_test))}


list_1 = ['a', 'b', 'c', 'd', 'e']
print(list_to_dict(list_1))