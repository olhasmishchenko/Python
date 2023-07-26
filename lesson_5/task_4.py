"""Даний перелік випадкових цілих чисел.
Замініть усі непарні числа списку нулями.
І виведете їхню кількість."""

list_random_num = [1, 33, 45, 44, 50]
count = 0
for i in range(len(list_random_num)):
    if list_random_num[i] % 2 != 0:
        list_random_num[i] = 0
        count += 1
print(list_random_num)
print("кількість непарних чисел", count)

