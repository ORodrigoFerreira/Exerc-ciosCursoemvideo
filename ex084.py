lista = []
pesados = []
leves = []

c = mai = men = 0

while True:
   nome = input('Nome: ')
   peso = int(input('Peso:'))


    lista.append([nome, peso])
    r = ' '

    if len(lista) == 0:
        mai = men = lista[0][1]
    if peso < men:
        men = peso
    if peso > mai:
        mai = peso

    while r not in 'sSnN':
        r = input('Deseja continuar? ').strip()
    if r in 'nN':
        break

for p in lista:
    if p[1] == men:
        leves.append(p[0])
    if p[1] == mai:
        pesados.append(p[0])

print(f'Foram cadastradas {len(lista)} pessoas')
print(f'As pessoas mais leve são:{leves}')
print(f'As pessoas mais pesadas são: {pesados}')
