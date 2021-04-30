lista = ('Lápis', 1.75,
         'Caderno', 5.6,
         'Mochila', 120.2,
         'Caneta', 2.5)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R${pos:.2f}')

