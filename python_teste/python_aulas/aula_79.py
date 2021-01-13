numeros = []
opção = ''
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opção not in 'SN':
        opção = str(input('Quer continuar? ')).strip().upper()[0]
    if opção == 'N':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')