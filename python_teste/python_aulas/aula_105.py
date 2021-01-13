dict = {}


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos (aceitar varias)
    :param sit: (valor opcional) indicando se deve ou não adcioanar a situação
    :return: Dicionario com varias informaçõees sobre asituação da turma
    """
    soma = maior = menor = 0
    for k, v in enumerate(n):
        soma += v
    total = len(n)
    dict['Total'] = total
    for k, v in enumerate(n):
        if k == 0:
            maior = menor = v
        else:
            if v > maior:
                maior = v
            elif v < menor:
                menor = v
    dict['Maior'] = maior
    dict['Menor'] = menor
    dict['Média'] = soma / len(n)
    if sit:
        if dict['Média'] >= 7:
            dict['Situação'] = 'BOA'
        elif 5 <= dict['Média'] <= 6.9:
            dict['Situação'] = 'RAZOAVEL'
        else:
            dict['Situação'] = 'RUIM'
    return dict



# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
help(notas)
