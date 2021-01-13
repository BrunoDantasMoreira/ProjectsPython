salario = float(input('Qual o salario do funcionario? R$'))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)
print('O salario do funcionario que é de {}R${:.2f}{}, com o aumento ficará de {}R${:.2f}{}'.format('\033[31m', salario, '\033[m', '\033[4;32m', aumento, '\033[m'))
