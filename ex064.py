n = 0
c = 0
n = int(input('Digite um número(999 para parar)'))
while n != 999:
    c += n
    n = int(input('Digite um número(999 para parar)'))
print('A soma dos valores digitados é ', c)
