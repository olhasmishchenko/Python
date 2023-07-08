import random
result_rand = random.randint(1, 10)
game_try = 0
while game_try < 3:
    print(f' Try № {str(game_try + 1)}')
    num = int(input('Please give me number from 1 to 10: '))
    game_try += 1
    if num > result_rand or (num < result_rand):
        print('You lose!')
    elif num == result_rand:
        print('You won!')
        break
if game_try >= 4:
    print('You lose!')