v = int(input('Digite a velocidade do carro: '))
if v > 80:
    m = (v - 80) * 7
    print('O carro utrapassou o limite de velocidade! ')
    print('A multa que deverá pagar é de R${:.2f}'.format(m))
else:
    print('O carro não ultrapassou o limite de velocidade! ')
