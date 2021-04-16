l1 = float(input('Lado 1'))
l2 = float(input('Lado 2'))
l3 = float(input('Lado 3'))

a = l1 + l2
b = l1 + l3
c = l2 + l3

if l1 <= c and l2 <= b and l3 <= a:
    print('Esses comprimentos de reta formam um triângulo!')
else:
    print('Esses comprimentos de reta não formam um triângulo!')
