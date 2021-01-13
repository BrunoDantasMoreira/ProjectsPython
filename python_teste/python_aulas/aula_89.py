ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*36)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe) '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas do aluno {ficha[opc][0]} são {ficha[opc][1]}')
print('FIM')