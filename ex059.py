a = float(input('Digite dois valores.\n Primeiro número:'))
b = float(input('Segundo número:'))
c = 0
s = 0

while c != 5:
    print('Que ação você quer tomar?')
    c = int(input('''Digite:'
                  [1] Somar
                  [2] Multiplicar
                  [3] Maior
                  [4] Novos Números
                  [5] Sair do programa'''))
    if c == 1:
        s = a + b
    elif c == 2:
        s = a*b
    elif c == 3:
        s = a
        if b > a:
            s = b
    elif c == 4:
        a = int(input('Digite os novos números. \n Primeiro número:'))
        b = int(input('Segundo Número:'))
    else:
        print('Valor inválido. Digite novamente!')
    if c != 5:
        print(s)
print('Fim')
