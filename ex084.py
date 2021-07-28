lista = []

while True:
    lista.append([input('Nome: '), input('Peso: ')])
    r = ' '
    while r not in 'sSnN':
        r = input('Deseja continuar? ').strip()
    if r in 'nN':
        break

print(f'Foram cadastradas {len(lista)+1} pessoas')
