from random import randint
print('Eu pensei em um número, tente adivinhar. ')
n  = randint(0, 10)
r = 0
t = 0
while r != n:
    r = int(input('Em qual numero eu pensei? '))
    t += 1
    if r > n:
        print('Um pouco MENOS!')
    elif r < n:
        print('Um pouco MAIS')
print('Você acertou, eu pensei no numero {}'.format(n))
print('Você acertou em {} tentativas! '.format(t))
if t < 3:
    print('Você acertou muito rapido, PARABÉNS')
