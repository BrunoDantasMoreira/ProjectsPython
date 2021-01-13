lista = ('lapis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120,
         'Canetas', 22.30,
         'Livro', 34.90)
print('-'*40)
print(f'{"Listagem de preços":^40}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<40}', end=' ')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-'*40)
