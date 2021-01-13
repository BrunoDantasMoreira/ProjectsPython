peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual a sua altura? (m)'))
IMC = peso / (altura * altura)
print('O seu IMC é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está ABAIXO DO PESO normal! ')
elif 18.5 <= IMC < 25:
    print('Você está na faixa de PESO NORMAL! ')
elif 25 <= IMC < 30:
    print('Você está em SOBRE PESO! ')
elif 30 <= IMC <= 40:
    print('Você está em OBESIDADE! ')
else:
    print('Você está em OBESIDADE MORBIDA, cuidado! ')
