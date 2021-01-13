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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: favor, digite um número inteiro válido. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interronpida pelo usuario\033[m')
            return 0
        else:
            return n


# Programa Principal
i = leiaInt('Digite um numero Inteiro: ')
r = leiaFloat('Digite um número Real: ')
print(f'\nO valor inteiro digitado foi {i} e o valor real foi {r}')
