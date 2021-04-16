n = int(input('Número de pessoas'))

soma = 0
velho = 0
homem = ''
mulher = 0

for c in range(1, n + 1):
    print('{:-^15}'.format('{}ªpessoa'.format(c)))
    a = input('Nome:').capitalize()
    b = int(input('Idade:'))
    c = input('Sexo( M OU F):').upper()
    soma += b
    if c == 'M' and b > velho:
        velho = b
        homem = a
    if c == 'F' and b < 20:
        mulher += 1
media = soma/n

print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho é o {}.'.format(homem))
print('O número de mulheres com menos de 20 anos é {}.'.format(mulher))
