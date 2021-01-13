print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
cont = 0
while True:
    if valor >= ced:
        valor -= ced
        cont += 1
    else:
        if cont > 0:
            print(f'Total de {cont} cédulas de R${ced}')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if valor == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV!')




