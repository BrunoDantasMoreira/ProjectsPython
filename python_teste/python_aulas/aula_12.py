preço = float(input('Qual o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promação com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
