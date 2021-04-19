maior = homem = garota = 0

while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M OU F] ')
    if idade > 18:
         maior += 1
    if sexo in 'Mm':
         homem += 1
    if sexo in 'Ff' and idade < 20:
        garota += 1
    con = input('Quer continuar?').strip().upper()[0]
    if con in 'N':
        break
print(f'O total de pessoas com mais de 18 anos é: {maior}')
print(f' {homem} pessoas são homens;')
print(f'e {garota} são mulheres com menos de 20 anos.')
