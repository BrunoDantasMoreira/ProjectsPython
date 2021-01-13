from random import randint
lista = []


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        s = randint(1, 10)
        lista.append(s)
        print(s, end=' ')


def somapar():
    soma = 0
    for a in lista:
        if a % 2 == 0:
            soma += a
    print(f'\nSomando os valores pares de {lista}, temos {soma}')



sorteia()
somapar()
