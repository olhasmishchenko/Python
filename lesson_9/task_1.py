"""Написати функцію, яка рахуватиме кількість очок футбольної команди.
Перемога дає 3 очки, нічия 1 очко, поразка -1 очко.
Функція приймає три аргументи – win, draw, loss."""


def count_points(win: int, draw: int, loss: int):
# win - quantity of wins
# draw - quantity of draw
# loss - quantity of loss
# points - quantity of points
    points = win * 3 + draw * 1 - loss
    return points


print(f'Quantity of points of the football team {count_points(10, 2, 3)}')