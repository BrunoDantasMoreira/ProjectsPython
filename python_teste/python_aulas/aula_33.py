a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
if b < a and b < c:
    print('O menor número é o {}{}{}'.format('\033[31m', b, '\033[m'))
if c < a and c < b:
    print('O menor número é o {}{}{}'.format('\033[31m', c, '\033[m'))
if a < b and a < c:
    print('O menor número é o {}{}{}'.format('\033[31m', a, '\033[m'))
if b > a and b > c:
    print('E o maior número é {}{}{}'.format('\033[31m', b, '\033[m'))
if c > a and c > b:
    print('E o maior número é {}{}{}'.format('\033[31m', c, '\033[m'))
if a > b and a > c:
    print('Eo maior número é {}{}{}'.format('\033[31m', a, '\033[m'))
