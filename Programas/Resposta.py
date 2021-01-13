from random import randint

resposta = randint(1, 5)
pergunta = str(input('Faça sua pergunta: '))

if resposta == 1:
    print('sim')

if resposta == 2:
    print('Não')

if resposta == 3:
    print('Não sei')

if resposta == 4:
    print('Você que decide')

