vogais = ('A', 'E', 'I', 'O', 'U')
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR')

for c in palavras:
    print(f'\nNa palavra {c} temos ', end='')
    for letra in c:
        if letra in vogais:
            print(letra, end=' ')

