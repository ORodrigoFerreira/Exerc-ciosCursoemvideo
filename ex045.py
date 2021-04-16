from random import randint
from time import sleep
jogo = ['PEDRA', 'PAPEL', 'TESOURA']
computador = jogo[randint(0, 2)]
jogador = input('PEDRA, PAPEL ou TESOURA?').upper()
print('-=-'*10)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-=-'*10)
print(computador)
if computador == jogador:
    print('Empate! Jogue mais uma vez.')
elif computador == 'PEDRA' and jogador == 'TESOURA':
    print('Você perdeu, mas não desista, continue tentando!')
elif computador == 'PAPEL' and jogador == 'PEDRA':
    print('Você perdeu, mas não desista, continue tentando.')
elif computador == 'TESOURA' and jogador == 'PAPEL':
    print('Você perdeu, mas não desista, continue tentando.')
else:
    print('PARABÉNS! Você ganhou.')
