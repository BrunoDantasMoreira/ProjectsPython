lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = soma3 = maior = 0
for c in range(0, 3):
    for s in range(0, 3):
        lista[c][s] = int(input(f'Digte um valor para [{c}, {s}]: '))
        if lista[c][s] % 2 == 0:
            somap += lista[c][s]
        if c == 1:
            if s == 0:
                maior = lista[c][s]
            elif lista[c][s] > maior:
                maior = lista[c][s]

soma3 = lista[0][2] + lista[1][2] + lista[2][2]
print('-='*30)
for c in range(0, 3):
    for s in range(0, 3):
        print(f'[{lista[c][s]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {somap}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior}')


