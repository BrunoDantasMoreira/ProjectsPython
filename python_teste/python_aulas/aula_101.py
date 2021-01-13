def voto(num):
    from datetime import date
    global idade
    ano = date.now().year
    idade = ano - nasc
    if idade < 16:
        return False
    elif 18 <= idade <= 65:
        return True


# Programa Principal
idade = 0
print('_'*30)
nasc = int(input('Em que ano você nasceu? '))
voto1 = voto(nasc)
print(f'Com {idade} anos: ', end='')
if voto(voto1) and idade <= 65:
    print('VOTO OBRIGATORIO')
elif 16 < idade < 18 or idade >= 65:
    print('VOTO OPCIONAL')
else:
    print('NÃO VOTA')