valor = int(input('Quanto irá sacar?'))
nota = 50
print('Você receberá:')
while True:
    n = valor//nota
    print(f' {n} notas de R${nota} ')
    valor %= nota
    if nota == 50:
        nota = 20
    elif nota == 20:
        nota = 10
    elif nota == 10:
        nota = 1
    if valor == 0:
        break
