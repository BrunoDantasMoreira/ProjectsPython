def maior(*n):
    cont = maior = 0
    print('-='*30)
    print('\nAnalisando os valores passados...')
    for valor in n:
        print(f'{valor}', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo!')
    print(f'O maior valor foi {maior}')

#programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()