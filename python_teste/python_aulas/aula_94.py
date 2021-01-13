dict = {}
lista = []
soma = 0
while True:
    dict['nome'] = str(input('Nome: ')).capitalize()
    dict['sexo'] = str(input('Sexo: ')).strip().upper()[0]
    while dict['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        dict['sexo'] = str(input('Sexo: ')).strip().upper()[0]
    dict['idade'] = int(input('Idade: '))
    soma += dict['idade']
    lista.append(dict.copy())
    opção = str(input('Quer continuar? ')).strip().upper()[0]
    while opção not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        opção = str(input('Quer continuar? ')).strip().upper()[0]
    if opção == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'B) A media de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('D) As pessoas com idade maior que a média são ', end='')
for c in lista:
    if c['idade'] > media:
        print(f'{c["nome"]}', end=' ')
