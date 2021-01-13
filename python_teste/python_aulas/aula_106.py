from time import sleep


def ajuda(com):
    titulo(f'Acessando o manual de comando \'{com}\'\033[30;44m')
    print('\033[7;30m', end='')
    help(com)
    print('\033[m', end='')
    sleep(2)


def titulo(msg):
    tam = len(msg) + 4
    print('\033[30;42m', end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print('\033[40m', end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    titulo('Sistema de ajuda\033[30;42m')
    comando = str(input('Função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!\033[41m')