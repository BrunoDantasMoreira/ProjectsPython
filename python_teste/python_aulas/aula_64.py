n = cont = soma = 0
while n != 999:
    n = int(input('Digite um numero (999 para parar) : '))
    soma += n
    cont += 1
soma -= 999
cont -= 1
print('Você digitou {} números e a soma deles é igual a {}!'.format(cont, soma))