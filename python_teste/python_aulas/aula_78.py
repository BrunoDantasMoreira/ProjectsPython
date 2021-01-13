maior = menor = 0
valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('=-'*30)
print(f'Os valores digitados foram {valores}')
print(f'O maior valor digitado {maior} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
