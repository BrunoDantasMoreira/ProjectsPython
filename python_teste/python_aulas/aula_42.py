print('{}ANALISADOR DE TRIANGULOS{}'.format('\033[4;31m', '\033[m'))
n1 = int(input('Prinmeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if n1 + n2 > n3 and n2 + n3 > n1 and n3 + n1 > n2:
    print('Os segmentos acima PODEM FORMAR um trinagulo ', end='')
    if n1 == n2 == n3:
        print('EQUILATERO! ')
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print('ISÓSCELES! ')
    else:
        print('ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo! ')
