try:
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de valor que voê colocou')
except ZeroDivisionError:
    print('Não é possivel dividir o valor por zero')
except KeyboardInterrupt:
    print('O usuario preferio não informar os dados')
else:
    print(r)
finally:
    print('Volte sempre, obrigado')
