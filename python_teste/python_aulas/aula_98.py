from time import sleep

def contador(a, b, c):
    for x in range(a, b+1, c):
        print(x, end=' ')
        sleep(0.4)
    if a > b:
        for x in range(a, b-1, -c):
            print(x, end=' ')
            sleep(0.4)
    print(' => Fim')


#Programa Principal
print('-='*20)
print('Contagem de 1 até 10 contando de 1 em 1')
sleep(1)
contador(1, 10, 1)
print('-='*20)
print('Contagem de 10 até 0 contando de 2 em 2')
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar sua contagem! ')
inicio = int(input('início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

