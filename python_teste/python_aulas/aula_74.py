from random import randint
números = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('Os números sorteados foram: ', end='')
for n in números:
    print(f'{n} ', end='')
print(f'\nO maior números sorteado foi {max(números)}')
print(f'O menor número sorteado foi {min(números)}')