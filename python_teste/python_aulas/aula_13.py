salario = float(input('Qual o salario do Funcionario? R$'))
novo = salario + (salario * 15 / 100)
print('O funcionario que ganhava R${:.2f} com 15% de aumento ganhará R$0{:.2f}'.format(salario, novo))
