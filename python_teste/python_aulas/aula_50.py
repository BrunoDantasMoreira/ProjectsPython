count = 0
s = 0
for c in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(c)))
    if n % 2 == 0:
        s += n
        count += 1
print('Você digitou {} números pares e a soma entre eles é {}'.format(count,s))