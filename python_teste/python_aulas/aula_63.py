print('-'*30)
print('SEQUENCIA DE FIBONACCI')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 0
print('0 -> 1', end=' -> ')
while cont <= n:
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')