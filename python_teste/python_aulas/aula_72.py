lista = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezeceis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
while True:
    n = int(input('Digite um número entre 0 e 20:'))
    while n < 0 or n > 20:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {lista[n]}')
    o = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    while o not in 'SN':
        o = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if o == 'N':
        break
print('Fim')