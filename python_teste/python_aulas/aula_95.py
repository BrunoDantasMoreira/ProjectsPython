dict = dict()
gol = list()
lista = list()
while True:
    dict['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {dict["nome"]} jogou? '))
    gol.clear()
    for c in range(0, partidas):
        gol.append(int(input(f'    Quantos gols na {c}° partida? ')))
    dict['gols'] = gol[:]
    dict['total'] = sum(gol)
    lista.append(dict.copy())
    opc = str(input('Quer continuar? ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Quer continuar? ')).strip().upper()[0]
    if opc == 'N':
        break
print('-='*30)
print('cod', end='')
for i in dict.keys():
    print(f'{i:<15}', end='')
print()
print('-='*40)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)
while True:
    busca = str(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'ERRO, Não existe jogador com codigo da {busca}!')
    else:
        print(f' --- Levantamento do jogador {lista[busca]["nome"]}')
