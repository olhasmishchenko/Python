"""Дано два кортежі, напишіть функцію яка з'єднає їх в один dict:"""

def unite(tuple_1, tuple_2):
    return dict(zip(tuple_1, tuple_2))


coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
print(unite(coin, code))