dict = dict()
lista = list()

dict['nome'] = str(input('Nome: '))
dict['media'] = int(input(f'Media de {dict["nome"]}: '))
lista.append(dict.copy())
print('-='*30)
print(f'   - nome é igual á {dict["nome"]}')
print(f'   - media é igual á {dict["media"]}')
if dict['media'] < 5:
    print('   - e a situação é igual a reprovado')
elif 5.1 < dict['media'] < 7:
    print('   - e a situação é igual á recuperação')
else:
    print('   - e a situação é igual á aprovado')