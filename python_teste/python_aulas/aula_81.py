lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print('=-'*30)
print(f'Você digitou {len(lista)} elemntos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
