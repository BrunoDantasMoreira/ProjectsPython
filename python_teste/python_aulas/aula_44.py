print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] duas vezes no cartão
[ 4 ] três vezes ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    desconto = preço - (preço * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(preço, desconto))
elif opção == 2:
    desconto = preço - (preço * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(preço, desconto))
elif opção == 3:
    parcela = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
    print('O valor da sua compra se mantera R${:.2f} sem juros!'.format(preço))
elif opção == 4:
    parcelas = int(input('Quantas parcelas'))
    juros = preço + (preço * 20 /100)
    preçoparcelado = juros / parcelas
    print('Sua compra será parcelada {}x de R${:.2f} com juros. '.format(parcelas, preçoparcelado))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(preço, juros))
else:
    print('\033[31mOpção invalida')