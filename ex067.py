while True:
    n = int(input('Você que ver a tabuada de que valor? (Digite -1 para desligar)'))
    if n == -1:
        break
    for c in range(1, 11):
        print(f'{c:>4} x {n} = {c*n}')
print('FIM')
