n = int(input('Digite um número'))
r = 0
for c in range(2, n):
    if n % c == 0:
        r = r + 1

if r == 0 and n > 1:
    print('O número é \033[32;40m PRIMO.\033[m')
else:
    print('O número {} não é primo.'.format(n))
