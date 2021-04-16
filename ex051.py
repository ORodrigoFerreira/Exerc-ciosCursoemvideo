a1 = int(input('Digite o primeiro termo da PA'))
r = int(input('Digite a Razão da PA'))
n = int(input('Número de termos da PA'))

for c in range(a1, a1 + (n-1)*r + 1, r):
    print(c, end=' →')
