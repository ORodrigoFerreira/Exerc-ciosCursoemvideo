km = float(input('Qual a distância da sua viagem?  Km'))
if km <= 200:
    print('O preço da passagem será de R$', 0.5*km)
else:
    print('O preço da passagem será de R$', 0.45*km)
