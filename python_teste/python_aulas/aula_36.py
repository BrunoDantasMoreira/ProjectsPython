print('\033[4mOlá, eu precisarei fazer algumas perguntas antes de aprovar o emprestimo da compra da casa! \033[m')
valor = int(input('Qual o valor da casa? R$'))
sálario = int(input('Qual é o seu sálario? R$'))
ano = int(input('Em quantos anos você pretende pagar? '))
prestação = valor / (ano * 12)
minimo = sálario * 30 / 100
if prestação > minimo:
    print('\033[31mMe desculpe mas não é possivel fazer o emprestimo.')
    print('Pois o valor da mensalidade é muito alto para o seu salario de R${:.2f}! \033[m'.format(sálario))
else:
    print('Seu emprestimo foi aprovado, o valor da prestação mensal é de R${:.2f} no tempo de {} anos!'.format(prestação, ano))

