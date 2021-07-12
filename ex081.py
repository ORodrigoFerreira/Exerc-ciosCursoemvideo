lista = []
r = ' '
c = 0
while r not in 'Nn':
    lista.append(int(input('Digite um valor:  ')))
    r = ' '
    while r not in 'SsNn':
        r = input('Você quer continuar? [S/N]  ').strip()
    c += 1
print(f'Você digitou {c} elementos.')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O número 5 foi encontrado na lista.')
else:
    print('O núemro 5 não foi encontrado na lista')
