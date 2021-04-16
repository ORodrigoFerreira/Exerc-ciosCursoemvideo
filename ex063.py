print('=-='*10)
print('SEQUÊNCIA DE FIBONACCI')
print('=-='*10)

n = 0
j = int(input('Quantos termos da sequência de Fibonaccio você quer ver?'))
a = 1
b = 1


while n < j:
    if n < 2:
        c = 1
    else:
        c = a + b
        a = b
        b = c
    n += 1
    print(c, end=' → ' if n < j else '  FIM')
