a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Qual a razão da PA: '))
c = 10
n = 0
b = 0
j = c + b

while n < j:
    print(a)
    a += r
    n += 1
    if n == j:
        d = int(input('Quer ver mais quantos valores? '))
        j += d

print('Você pediu {} valores'.format(n))
