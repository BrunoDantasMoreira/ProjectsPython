from random import choice
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']
print('{:-^50}'.format(' \033[1;36mPEDRA, PAPEL E TESOURA\033[m '))
print('''SUAS OPÇÕES
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
player = int(input('Qual é a sua jogada? '))
print('\033[1;34mJO')
sleep(0.55)
print('KEN')
sleep(0.55)
print('PO!!!\033[m')
sleep(0.2)
bot = choice(lista)
print('-=' * 32)
if player == 1 and bot == 'Tesoura':
    print('Eu ganhei, eu joguei Papel e você jogou Pedra!')
elif player == 1 and bot == 'Pedra':
    print('Empatamos, ambos jogamos Pedra!')
elif player == 2 and bot == 'Pedra':
    print('PARABÉNS, você ganhou de mim, eu joguei Pedra e você jogou Papel!')
elif player == 2 and bot == 'Tesoura':
    print('Eu ganhei, eu joguei Tesoura e você jogou Papel!')
elif player == 2 and bot == 'Papel':
    print('Empatamos, ambos jogamos Papel!')
elif player == 3 and bot == 'Papel':
    print('PARABÉNS, você ganhou de mim, eu joguei Papel e você jogou Tesoura!')
elif player == 3 and bot == 'Pedra':
    print('Eu ganhei, eu joguei Pedra e você jogou Tesoura!')
elif player == 3 and bot == 'Tesoura':
    print('Empatamos, ambos jogamos Tesoura')
else:
    print('\033[31mOpção Invalida')
print('-=' * 32)