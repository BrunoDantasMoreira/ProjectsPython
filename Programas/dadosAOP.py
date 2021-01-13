# Este programa foi  feito com o objetivo de substituir os dados fisicos em um jogo de RPG que usa o mesmo sistema de OSNF

# Biblioteca
from time import sleep
from random import randint

while True:

    # Painel
    print('Opções:')
    print('---' * 10)
    print('[ 1 ] Rolar dados')
    print('[ 2 ] Rolar mais de um dado')
    print('[ 3 ] Sair')
    print('---' * 10)
    while True:
        op = int(input('O que você que fazer? '))
        if op == 1 or op == 2 or op == 3:
            break

    if op == 1:

        pontos = int(input('Quantos pontos você quer gastar? '))

        # Resultado dos dados
        escolhido = randint(1, 6) + pontos
        print('ROLANDO...')
        sleep(1)
        print('O numero escolhido é {}{}{}'.format('\033[1;34m', escolhido, '\033[m'))

    if op == 2:

        total = 0
        quantidade = int(input('Quantos dados você quer usar? '))
        pontos = int(input('Quantos pontos você quer gastar? '))
        for c in range(quantidade):
            escolhido = randint(1, 6) + pontos
            print('ROLANDO...')
            sleep(1)
            print('O numero escolhido é {}{}{}'.format('\033[1;34m', escolhido, '\033[m'))
            total += escolhido
        print(f'A soma dos dados é igual a {total}')
    
    if op == 3:
        break

# Fim
print('\033[31m-=-' * 10)
