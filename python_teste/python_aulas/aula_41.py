from datetime import date
ano= date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: {}MIRIM{}'.format('\033[34m', '\033[m'))
elif idade <= 14:
    print('Classificação: {}INFANTIL{}'.format('\033[34m', '\033[m'))
elif idade <= 19:
    print('Classificação: {}JUNIOR{}'.format('\033[34m', '\033[m'))
elif idade <= 25:
    print('Classificação: {}SENIOR{}'.format('\033[34m', '\033[m'))
else:
    print('Classificação: {}MASTER{}'.format('\033[34m', '\033[m'))
