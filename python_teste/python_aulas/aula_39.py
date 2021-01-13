from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
if idade < 18:
    alistamento = 18 - idade
    print('Você precisará se apresentar para o alistamento ')
elif idade == 18:
    print('Este ano você precisa se apresentar para o alistamento! ')
else:
    atrasado = idade - 18
    print('Você não precisa mais se apresentar para o alistamento, ')
if idade <= 17:
    anodealistamento = nascimento + 18
    print('O seu alistamento será em {}'.format(anodealistamento))
else:
    anodealistamento = nascimento + 18
    print('Seu alistamento foi em {}'.format(anodealistamento))
