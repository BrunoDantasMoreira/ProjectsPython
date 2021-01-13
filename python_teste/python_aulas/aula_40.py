n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('A média do aluno foi de {}{:.1f}{}, e infelismente ele foi reprovado!'.format('\033[4;31m', media, '\033[m'))
elif media == 5.0 or media <= 6.9:
    print('A média do aluno foi de {}{:.1f}{} e ele está de recuperação!'.format('\033[4;32m', media, '\033[m'))
elif media > 7.0:
    print('A média do aluno foi de {}{:.1f}{}, então ele está aprovado! '.format('\033[4;34m', media, '\033[m'))
