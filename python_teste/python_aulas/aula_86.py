lista = [[], [], []]
for c1 in range(0, 3):
    num = int(input(f'Digite um valor para [0, {c1}]: '))
    lista[0].append(num)
for c2 in range(0, 3):
    num = int(input(f'Digite um valor para [1, {c2}]: '))
    lista[1].append(num)
for c3 in range(0, 3):
    num = int(input(f'Digite um valor para [2, {c3}]: '))
    lista[2].append(num)
print('-='*30)
print(f'[{lista[0][0]:^5}][{lista[0][1]:^5}][{lista[0][2]:^5}]')
print(f'[{lista[1][0]:^5}][{lista[1][1]:^5}][{lista[1][2]:^5}]')
print(f'[{lista[2][0]:^5}][{lista[2][1]:^5}][{lista[2][2]:^5}]')