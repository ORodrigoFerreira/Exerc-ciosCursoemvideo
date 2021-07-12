numeros = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        numeros.append(n)
        maj = n
        print('Número inserido na posição 0')
    else:
        for i in range(0, len(numeros)):
            if n <= numeros[i]:
                numeros.insert(i, n)
                print(f'Número inserido na posição {i}')
                break
            elif n >= maj:
                maj = n
                numeros.append(n)
                print('Número adicionado no final')
                break
    c += 1
print(numeros)
