mais18 = masc = mulher = 0
opção = sexo = 'a'
while True:
    print('-'*30)
    print('     Cadastre uma pessoa')
    print('-'*30)
    idade = int(input('idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 30)
    while opção not in 'SM':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if opção == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'O total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {masc} homens cadastrados. ')
if mulher == 1:
    print('E temos 1 mulher com menos de 20 anos. ')
else:
    print(f'E temos {mulher} mulheres com menos de 20 anos')
