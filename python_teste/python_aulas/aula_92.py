from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Data de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*30)
for i, v in dados.items():
    print(f'   - {i} tem o valor {v}')
