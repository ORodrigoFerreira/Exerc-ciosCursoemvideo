casa = float(input('Qual o preço da casa?'))
sal = float(input('Qual o seu salário?'))
anos = int(input('Em quantos anos você quer pagar?'))

prestacao = casa / (12*anos)

if prestacao > 0.3*sal:
    print('Infelizmente você não poderá comprar esta casa.')
else:
    print('Parabéns! Você tem condições de comprar essa casa.')
