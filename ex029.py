vel = float(input('Qual a velocidade do carro?'))
if vel > 80:
    print('Você foi multado, pois estava {}Km/h acima do permitido.\nSua multa é de R${:.2f}.'.format(vel - 80, (vel - 80)*7))
else:
    print('Parabéns! Você está cumprindo a lei!')

