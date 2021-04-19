from random import randint
c = 0
p = ' '
print('-=-'*30)
print('{:^90}'.format('Par ou ímpar'))
print('-=-'*30)
while True:
    comp = randint(0, 10)
    jog = int(input('Escolha um número!!'))
    while p not in 'PpIi':
        p = input('Par ou ímpar?[P/I] ').strip().upper()
    c += 1
    if (comp + jog) % 2 == 0 and p in 'P':
        break
    elif (comp + jog) % 2 != 0 and p in 'I':
        break
    print('Você errou tente mais uma vez')

print(f'Parabéns você venceu e só precisou de {c} tentativas')
