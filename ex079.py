lista = []

while True:
    numero = int(input('Digite um valor'))
    if numero in lista:
        print('Número duplicado, não adicionado...')
    else:
        lista.append(numero)
        print('Número adicionado com sucesso...')
    opcao = ' '
    while opcao not in 'NnSs':
        opcao = str(input('Quer continuar? [S/N]')).upper().strip()
    if opcao == 'N':
        break
lista.sort()

print(lista)
