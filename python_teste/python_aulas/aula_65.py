num = cont = soma = igual = maior = menor = 0
r = 'a'
while r != 'N':
    num = int(input('Digite um número: '))
    igual = num
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    r = str(input('Quer continuar? ')).strip().upper()
media = soma / cont
print('FIM, {}'.format(media))
print('O maior numero lido foi {} e o menor foi {}!'.format(maior, menor))
