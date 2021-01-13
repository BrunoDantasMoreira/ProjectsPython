km = float(input('Digite a distancia da viagem em km: '))
if km <= 200:
    preço = km * 0.5
else:
    preço = km * 0.45
print('O preço que você vai pagar da viagem é {:.2f}'.format(preço))