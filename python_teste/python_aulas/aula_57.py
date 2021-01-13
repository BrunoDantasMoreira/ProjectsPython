s = str(input('Informe o seu sexo: [M/F] ')).upper().strip()[0]
while s!= 'M' and s != 'F':
    s = str(input('Dados invalidos. Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucusso! '.format(s))
