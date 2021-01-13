opção = 0
r = True
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while r == True:
    print('''MENU
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do pragrama''')
    opção = int(input('>>>>> Sua opção: '))
    if opção == 1:
        s = n1 + n2
        print('A soma entre eles é igual a {}'.format(s))
    elif opção == 2:
        m = n1 * n2
        print('A multiplição dos dois é igual a {}'.format(m))
    elif opção == 3:
        if n1 > n2:
            print('O maior número que você escolheu foi o {:.1f}'.format(n1))
        else:
            print('O maior número que você escolheu foi o {:.1f}'.format(n2))
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        r = False
    else:
        print('Opção invalida! ')
    print('-=-' * 20)
print('Fim')
