# Este programa foi  feito com o objetivo de substituir os dados fisicos em um jogo de RPG

# Library
from time import sleep
from random import randint


def question():
    global choise
    global attributes
    choise = int(input('\033[mQual dado você usará: D'))
    if choise == 100:
        attributes = int(input('Qual é o número dos seus atributos? '))


def rollDice():
    global chosen
    chosen = randint(1, choise)
    print('ROLANDO...')
    sleep(1)
    print('O numero escolhido é {}{}{}'.format('\033[1;34m', chosen, '\033[m'))


def resultAttributes():
    global action
    if choise == 100:
        if chosen <= attributes / 5:
            print('Você tirou EXTREMO!')
        elif chosen <= attributes * 2:
            print('Você tirou BOM!')
        elif chosen <= attributes:
            print('Você tirou NORMAL!')
        elif chosen > attributes:
            print('Você FALHOU!')


# Tittle
print('\033[31m-=-' * 10)
print('{:^32}'.format('\033[32m  DADOS VIRTUAIS'))

while True:
    print('\033[31m-=-\033[m' * 10)

    # Panel
    print('Opções:')
    print('---' * 10)
    print('[ 1 ] Rolar dados')
    print('[ 2 ] Rolar dados com penalidade')
    print('[ 3 ] Rolar dados com soma')
    print('[ 4 ] Rolar mais de um dado')
    print('[ 5 ] Sair')
    print('---' * 10)
    while True:
        op = int(input('O que você que fazer? '))
        if op == 1 or op == 2 or op == 3 or op == 4:
            break

    if op == 1:

        # Questions
        question()

        # Rusult of dice
        rollDice()

        # Result of attributes
        resultAttributes()

    if op == 2:

        # Questions
        question()

        # Result of dice
        rollDice()

        # Result of attributes
        resultAttributes()

        # Penalty

        # Result of dice
        chosen2 = randint(1, choise)
        print('ROLANDO...')
        sleep(1)
        print('O numero escolhido é {}{}{}'.format('\033[1;34m', chosen2, '\033[m'))

        # Result of attributes
        if choise == 100:
            if chosen2 <= attributes / 5:
                print('Você tirou EXTREMO!')
            elif chosen2 <= attributes / 2:
                print('Você tirou BOM!')
            elif chosen2 <= attributes:
                print('Você tirou NORMAL!')
            elif chosen2 > attributes:
                print('Você FALHOU!')

        if chosen > chosen2:
            print('O DADO CONSIDERADO SERÁ O PRIMEIRO')
        else:
            print('O DADO CONSIDERADO SERÁ O SEGUNDO')

    if op == 3:

        # Questions
        question()
        sum = int(input('Quanto você quer somar? '))

        # Result of dice
        chosen = randint(1, choise) + sum
        print('ROLANDO...')
        sleep(1)
        print('O numero escolhido é {}{}{}'.format('\033[1;34m', chosen, '\033[m'))

        # Result of attributes
        resultAttributes()

    if op == 4:

        total = 0
        question()
        aumont = int(input('Quantos dados você quer usar? '))
        for c in range(aumont):
            rollDice()
            total += chosen
        print(f'A soma dos dados é igual a \033[31m{total}\033[31m')

    if op == 5:
        break

# End
print('\033[31m-=-' * 10)
