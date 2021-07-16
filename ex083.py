e = input('Digite uma expressão matemática:  ')
a = b = 0
for i, v in enumerate(e):
    if v == '(':
        a += 1
    elif v == ')':
        b += 1
if a == b:
    print('Expressão válida')
else:
    print('Expressão inválida')
