from random import randint

computador = randint(1, 11)

while True:
    jogador = int(input('Em qual número eu pensei? '))
    if jogador > computador:
        print('menos')
    elif jogador < computador:
        print('mais')
    elif jogador == computador:
        print(f'Parabéns você acertou, eu pensei em {computador}')
        break