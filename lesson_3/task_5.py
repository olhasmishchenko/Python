num = int(input('Please give me number: '))
num_2 = 1
for i in list(range(1, num + 1)):
    num_2 = num_2 * i
print(f'n! = {num_2}')