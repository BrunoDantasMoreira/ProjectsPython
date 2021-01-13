n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o ultimo número: '))
lista = (n1, n2, n3, n4)
print(f'Você digitou o valores \033[34m{lista}\033[m')
print(f'O valor 9 apareceu \033[34m{lista.count(9)}\033[m vezes')
if lista.count(3) == 0:
    print('O valor 3 não foi digitado em nenhuma posição!')
else:
    print(f'O valor 3 apareceu na \033[34m{lista.index(3)+1}° posição\033[m')
print('O valores pares digitados foram: \033[34m', end='')
if n1 % 2 == 0:
    print(n1, end=' ')
if n2 % 2 == 0:
    print(n2, end=' ')
if n3 % 2 == 0:
    print(n3, end=' ')
if n4 % 2 == 0:
    print(n4, end='\033[m ')
