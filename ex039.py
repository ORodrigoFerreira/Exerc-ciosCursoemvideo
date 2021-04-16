from datetime import datetime
nascimento = int(input('Em que ano você nasceu?'))
hoje = datetime.now().year
idade = hoje - nascimento

if idade < 18:
    print('Calma! A sua hora vai chegar\n Faltam {} anos.'.format(18 - idade))
elif idade == 18:
    print('Chegou a sua hora! Entre no site alistamentomilitar.com.br.')
else:
    print('Já passou a sua vez, você já se alistou, né?\n Já passou {} ano/anos.'.format(idade - 18))
