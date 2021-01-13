from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sitema'])
    if resposta == 1:
        # opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar uma nova pessoa
        cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Fim')
        break
    else:
        print('\033[31mErro: Digite uma opção valida')
