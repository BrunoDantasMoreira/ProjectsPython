num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases de conversão:
[ 1 ] conversor para BINARIO
[ 2 ] conversor para OCTAL
[ 3 ] conversor para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECILMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mComando não conhecido')