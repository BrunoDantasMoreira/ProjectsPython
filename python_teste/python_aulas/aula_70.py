opção =  menorp = 'a'
cont = soma = produto1000 = maior = menor = 0
print('-'*30)
print('      LOJA SUPER BARATÃO')
print('-'*30)
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += preço
    cont += 1
    if preço > 1000:
        produto1000 += 1
    if cont == 1:
        maior = menor = preço
        menorp = produto
    else:
        if preço > maior:
            maior = preço
        elif preço < menor:
            menor = preço
            menorp = produto
    if opção == 'N':
        break
print('------ FIM DO PROGRAMA ------')
print(f'O total da compra foi de R${soma:.2f}')
if produto1000 == 1:
    print('Temos um produto custando mais de R$1000.00')
else:
    print(f'Temos {produto1000} produtos custando mais de R$1000.00 ')
print(f'O produto mais barato foi {menorp} que custa {menor}')
