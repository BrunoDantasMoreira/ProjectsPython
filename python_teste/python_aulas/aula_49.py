n = int( input('Digite um número para ver sua tabuada: '))
s = 0
for c in range(1, 11):
    s = n * c
    print('{} x {} = {}'.format(n, c, s))