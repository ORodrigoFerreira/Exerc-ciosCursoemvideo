from random import randint
from time import sleep
print('-=-'*10)
j = int(input('Em que número eu pensei?'))
print('-=-'*10)
c = randint(1, 10)
a = 1

while j != c:
    sleep(1)
    print('Você errou,', end='')
    if j < c:
        print('É um número maior!!')
    elif j > c:
        print('É um número menor!!')
    j = int(input('tente mais uma vez!'))
    a += 1

p = ''
if a > 1:
    p = 's'
print('\033[31;40m Parabéns, você acertou! E só levou \033[33;40m {} \033[31;40m tentativa{}! \033[m'.format(a, p))

