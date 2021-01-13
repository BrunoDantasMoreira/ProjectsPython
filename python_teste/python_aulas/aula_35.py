print('{}ANALISADOR DE TRIANGULOS{}'.format('\033[4;31m', '\033[m'))
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Os segmentos acima PODEM FORMAR um triangulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo!')
