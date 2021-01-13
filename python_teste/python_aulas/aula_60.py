n = int(input('Digite um número para saber seu fatorial: '))
i = n
v = 0
m = 1
s = 1
print('{}! = '.format(i), end='')
while n != 1:
    s += 1
    m *= s
    v = n - 1
    f = n * v
    print('{}'.format(n), end=' x ')
    n -= 1
print('1 = {}'.format(m))
