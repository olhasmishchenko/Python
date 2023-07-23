# Програма запитує введення послідовності цілих
# невідємних чисел, доки не буде введено 0.
# Як тільки буде введено 0 (нуль), програма повинна порахувати та вивести на екран:

numbers = []
while True:
    number = int(input("Введiть число: "))
    if number == 0:
        break
    numbers.append(number)
print(f'Список {numbers}')

#кількість введених чисел (завершальний 0 не рахується)
print(f'кількість введених чисел {len(numbers)}')

#їхню суму


def sum(numbers):
    amount = 0
    for number in numbers:
        amount += number
    return amount


amount = sum(numbers)
print(f'сума {amount}')
#- добуток


def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


result = multiply(numbers)
print(f'добуток {result}')

#- середнє арифметичне (крім завершального числа 0)
result_1 = int(sum(numbers) / len(numbers))
print(f'середнє арифметичне {result_1}')

# Визначити значення та порядковий номер найбільшого
# елемента послідовності. Якщо найбільших елементів є кілька виведіть
# порядковий номер першого з них. Нумерація елементів починається з 1

max_number = max(numbers)
max_index = numbers.index(max_number) + 1
print(f'значення найбільше {max_number}, порядковий номер {max_index}')

#- визначити кількість парних та непарних елементів у послідовності

num_1 = 0
num_2 = 0
for number in numbers:
    if number % 2 == 0:
        num_1 += 1
    else:
        num_2 += 1
print(f'кількість парних {num_1}, кількість непарних {num_2}')


#- Визначити значення другого за величиною елемента в цій послідовності
print(f'другий за величиною елемент {sorted(numbers)[-2]}')

#- визначте, скільки елементів цієї послідовності дорівнюють її найбільшому елементу
print(f'Кількість елементів, які дорівнюють найбільшому елементу {numbers.count(max_number)}')






