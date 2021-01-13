num = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}° valor: '))
    if n % 2 == 0:
        num[0].append(n)
    if n % 2 == 1:
        num[1].append(n)
num[0].sort()
num[1].sort()
print('=-'*30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'E os valores ímpares digitados foram: {num[1]}')
