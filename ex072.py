extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número entre 0 e 20: '))

while n < 0 or n > 20:
    n = int(input('Esse valor não está entre 0 e 20.'
                  'Digite novamente'))
print(f'Você digitou o número {extenso[n]}.')
