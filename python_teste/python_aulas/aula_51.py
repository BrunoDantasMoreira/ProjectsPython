pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print(' - ' * 10)
print('Os primeiros 10 termos são: ', end='')
print(' - ' * 20)
decimo = pt + (10 - 1) * r
for c in range(pt, decimo + r, r):
    print(c, end=' -> ')
print('Acabou!')
print(' - ' * 30)
