list_1 = [1, 4, 2, 1, 5]
list_2 = [4, 2, 7, 9]
#числа, що містяться одночасно як у першому списку, так і в другому
print("Наявнi як у першому списку, так і в другому")
for i in list_1:
    if i in list_2:
        print(i)
#числа, що містяться в першому, але відсутні в другому
print('Вiдсутнi у другому списку')
for i in list_1:
    if i not in list_2:
        print(i)
#тільки унікальні для першого та другого списків
print('Тільки унікальні для першого та другого списків')
list_3 = set(list_1 + list_2)
for i in list_3:
    if i in list_1 and i not in list_2:
        print(i)
    elif i in list_2 and i not in list_1:
        print(i)