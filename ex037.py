n = int(input('Escolha um número'))
e = int(input('Digite 1 para converter em binário\n'
              '2 para octal\n'
              'e 3 para hexadecimal.'))

if e == 1:
    print('O número {} em BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif e == 2:
    print('O número {} em OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif e == 3:
    print('O número {} em HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Entrada inválida')
