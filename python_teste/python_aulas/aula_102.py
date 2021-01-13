def fatorial(n=0 , show=False):
    """
    Caulcula o fatorial de um número
    :param n:O número a ser calculado
    :param show:(opçional) morstra ou não a conta
    :return: O valor do Fatorial de um número n
    """
    i = n
    v = 0
    m = 1
    s = 1
    if show:
        print(f'{i}! = ', end='')
        while n != 1:
            s += 1
            m *= s
            v = n - 1
            f = n * v
            print('{}'.format(n), end=' x ')
            n -= 1
        print('1 = {}'.format(m))
    else:
        while n != 1:
            s += 1
            m *= s
            v = n - 1
            f = n * v
            n -= 1
        print(m)


# Programa Principal
fatorial(3, True)
help(fatorial)

