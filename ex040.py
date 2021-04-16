p1 = float(input('Primeira nota'))
p2 = float(input('Segunda nota'))
media = (p1+p2)/2

if media < 5:
    print('Sinto muito, você foi reprovado. Tente novamente.')
elif 5 <= media < 6.9:
    print('Você está de recuperação. A esperança é a última que morre!')
else:
    print('Parabéns, você foi aprovado! Pode ir curtir as férias.')
