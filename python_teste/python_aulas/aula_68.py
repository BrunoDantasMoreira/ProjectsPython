from random import randint
jogador = cont = 0
computador = randint(1, 10)
pi = 'a'
print('=-=' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 10)
while True:
    cont += 1
    jogador = int(input('Diga um valor: '))
    pi = str(input('Par ou Ìmpar? [P/Í]')).strip().upper()[0]
    while pi not in 'PIÌ':
        pi = str(input('Par ou Ìmpar? [P/Í]')).strip().upper()[0]
    print('-'*30)
    soma = jogador + computador
    if soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total {soma}, DEU PAR!')
    elif soma % 2 == 1:
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total {soma}, DEU ÍMPAR')
    print('-'*30)
    if pi in 'P' and soma % 2 == 0:
        print('VOCÊ GANHOU!')
        print('Vamos jogar novamente.')
    elif pi in 'IÌ' and soma % 2 == 1:
        print('VOCÊ GANHOU!')
        print('Vamos jogar novamente.')
    else:
        print('VOCÊ PERDEU!')
        print('=-='*10)
        break
if cont == 1:
    print('GAME OVER! Você venceu 1 vez')
else:
    print(f'GAME OVER! Você venceu {cont} vezes.')
