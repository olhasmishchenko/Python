#Дано два цілих числа 'A' і 'В'. Виведіть усі числа від `A` до `B`
#включно, в порядку зростання,
#якщо `A < B`, або в порядку зменшення в іншому випадку.

a = int(input("Надрукуй перше число: "))
b = int(input('Надрукуй друге число: '))

if a < b:
    for i  in range(a, b + 1):
        print(i)
elif a > b:
    for i in range(a, b - 1, -1):
        print(i)
else:
    print("Перше та друге число мають бути рiзними")
