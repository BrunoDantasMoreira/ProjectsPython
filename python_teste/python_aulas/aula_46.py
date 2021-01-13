from time import sleep
print('{:^50}'.format('\033[34mCONTAGEM REGRESSIVA\033[m'))
for c in range(10, - 1, -1):
    print(c)
    sleep(1)
print('FIM')
