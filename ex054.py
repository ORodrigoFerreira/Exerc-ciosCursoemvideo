from datetime import datetime

v = 0
n = 0
for c in range(1, 8):
    ano = int(input('Em que ano você nasceu?'))
    idade = datetime.now().year - ano
    if idade >= 18:
        v += 1
    else:
        n += 1

print('São {} maiores de idade\n  e {} menores de idade.'.format(v, n))

