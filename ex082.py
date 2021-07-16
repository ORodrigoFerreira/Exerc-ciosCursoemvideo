lista = []
pares = []
impares = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = ' '
    while r not in 'SsNn':
        r = input('Você quer continuar?  ')
    if r in 'nN':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'A lista completa de números digitados é: {lista}')
print(f'Sendo que os números {pares} são pares')
print(f'E os {impares} são ímpares.')