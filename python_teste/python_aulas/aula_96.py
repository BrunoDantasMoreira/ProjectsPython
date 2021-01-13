def area(a, b):
    ar = a * b
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {ar:.1f}m²')


#Programa Principal
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(largura, comprimento)
