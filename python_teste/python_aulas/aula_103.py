def ficha(jogador='<Desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato!')


# Progrmama Principal
j = str(input('Nome do jogador: ')).capitalize()
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gol=g)
else:
    ficha(j, g)
    