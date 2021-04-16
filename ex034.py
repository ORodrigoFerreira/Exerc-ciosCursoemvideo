sal = float(input('Qual o seu salário?'))
if sal >= 1250:
    print('O seu novo salário será de R${:.2f}'.format(1.1*sal))
else:
    print('O seu novo salário será de R${:.2f}'.format(1.15*sal))
