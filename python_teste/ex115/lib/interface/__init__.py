def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interronpida pelo usuario!\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '\033[m-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m[ {c} ] \033[34m{item}')
        c += 1
    print('\033[m', linha())
    opc = leiaInt('Sua Opção: ')
    return opc