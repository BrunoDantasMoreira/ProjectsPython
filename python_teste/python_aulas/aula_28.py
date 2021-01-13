from random import randint
from time import  sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Eu estou pensando em um número de 0 a 5.')
jogador = int(input('Em que número eu estou pensando? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns, você acertou! ')
else:
    print('Você errou, eu estava penasando em {} e não no {}!'.format(computador, jogador))
print('-=-' * 20)
