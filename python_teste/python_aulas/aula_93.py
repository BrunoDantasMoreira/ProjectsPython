dict = dict()
lista = list()
dict['nome'] = str(input('Nome do jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas {dict["nome"]} jogou? '))
for c in range(0, partidas):
    lista.append(int(input(f'    Quantos gols na {c}° partida? ')))
dict['gols'] = lista[:]
dict['total'] = sum(lista)
print('-='*30)
print(dict)
print('-='*30)
for k, v in dict.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {dict["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(lista):
    print(f'   => Na partida {i},  fez {v} gols.')
print(dict['total'])


