expor = str(input('Digite a exprssão: '))
pilha = []
for simb in expor:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print('=-'*30)
if len(pilha) == 0:
    print('A expressão é \033[34mvalida\033[m! ')
else:
    print('A expressão é \033[31minvalida\033[m! ')
