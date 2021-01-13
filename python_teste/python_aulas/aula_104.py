def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[31mDigite um número valido!\033[m')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um numero: ')
print(f'Você acabou de digtar o número {n}')
