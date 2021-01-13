n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[m')
print('O número {} foi dividido {} veses'.format(n, tot), end='. ')
if tot == 2:
    print('Então ele é primo! ')