c = t = tm1000 = 0

while True:
    nome = input('Nome do Produto: ')
    preco = float(input('Preço do Produto: '))
    c += 1
    t += preco
    if c == 1:
        maiorp = menorp = preco
        maior = menor = nome
    else:
        if preco > maiorp:
            maiorp = preco
            maior = nome
        elif preco < menorp:
            menorp = preco
            menor = nome

    if preco > 1000:
        tm1000 += 1
    r = ' '
    while r not in 'NnSs':
        r = input('Quer continuar? [S/N] ').strip()
    if r in 'Nn':
        break
print(f'O total da compra foi de R${t}')
print(f'Temos {tm1000} produtos custando mais de R$1000,00')
print(f'O prouto mais caro foi o {maior} custando R${maiorp:.2f} e', end=' ')
print(f'O mais barato foi o {menor} custando R${menorp:.2f}')

