num = float(input('Please give me number: '))
list_obj = tuple([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
if num in list_obj:
    print(f'{num} in list')
elif abs(num) in list_obj:
    print(f'{num} in list')
else:
    print(f'{num} not in list')




