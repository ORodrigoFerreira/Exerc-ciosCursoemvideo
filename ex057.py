s = input('Digite o sexo').strip().lower()[0]
while s not in 'mf':
    print('Dados inválidos, informe novamente.')
    s = input('M/F?').strip().lower()[0]
print('Registrado com sucesso.')
