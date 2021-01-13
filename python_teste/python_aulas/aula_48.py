soma = 0
s = 0
for c in range(0, 501, 3):
    if c % 2 == 1:
        print(c)
        n = c
        soma = soma + 1
        s += n
print('A soma entre os {} números é {}'.format(soma, s))