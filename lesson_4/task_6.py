#Даний список чисел. Визначте, скільки в цьому списку елементів,
#які більше двох своїх сусідів (ліворуч і праворуч),
#та виведіть кількість таких елементів. Крайні елементи списку
#ніколи не враховуються, оскільки вони мають недостатньо сусідів.

list_1 = [1, 4, 2, 1, 5]
print(list_1)
x = 0
for i in range(1, len(list_1) - 1):
    if list_1[i] > list_1 [i - 1] and list_1[i] > list_1[i + 1]:
        x += 1
print(x)