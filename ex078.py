lista = []
c = mai = men = 0

while True:
    valor = int(input(f'Digite o valor da posição {c} '))
    lista.append(valor)
    if c == 0:
        mai = men = valor
    elif valor > mai:
        mai = valor
    elif valor < men:
        men = valor

    c += 1
    if c == 5:
        break

print(f'Os números digitados foram {lista}')
print(f'O maior valor digitado foi {mai} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}', end='...')
print()
print(f'O menor valor digitado foi {men} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}', end='...')


