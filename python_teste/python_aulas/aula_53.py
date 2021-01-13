frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print(junto, inverso)
if junto == inverso:
    print('È um palindromo')
