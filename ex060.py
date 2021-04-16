n = int(input('Digite o número que você quer saber o fatorial.'))
f = 1

while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    f *= n
    n -= 1
print(f)
