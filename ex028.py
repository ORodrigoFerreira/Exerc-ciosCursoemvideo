from random import randint
from time import sleep
n = randint(0, 5)
print(('=-')*10)
m = int(input('Escolha um número entre 1 e 5'))
print(('=-')*10)
print('Processando ....')
sleep(3)
if n == m:
    print('Você ganhou')
else:
    print('Você perdeu')
print('Fim de Jogo')

