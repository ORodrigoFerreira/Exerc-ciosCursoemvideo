numeros = (int(input('Digite um valor')), int(input('Digite um valor')),
           int(input('Digite um valor')),int(input('Digite um valor')),int(input('Digite um valor')))

print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O primeiro 3 apareceu na posição {numeros.index(3)+1}.')
else:
    print('O número 3 não apareceu.')
print('Os valores pares são: ', end= '')
for c in numeros:
    if c % 2 == 0:
        print(c, end=', ')
