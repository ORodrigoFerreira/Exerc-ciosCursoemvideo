n = int(input('Qual tabuado você quer?'))
for c in range(1, 11):
    print('{:^3}x{:2} = {}'.format(c, n, c*n))
