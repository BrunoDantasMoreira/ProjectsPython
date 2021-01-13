from datetime import date
ano = date.today().year
j = 0
v = 0
for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    ano = date.today().year
    idade = ano - nascimento
    if idade > 21:
        v += 1
    else:
        j += 1
idade = ano - nascimento
print('{} velhos e {} jovens!'.format(v, j))
