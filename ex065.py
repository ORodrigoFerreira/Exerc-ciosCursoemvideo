import emoji

print('-=-'*30)
n = int(input('Digite um número: '))
print('-=-'*30)
j = input('Quer continuar?[S/N] ')
soma = n
maior = n
menor = n
c = 1
while j != 'n':
    print('-=-'*30)
    n = int(input('Digite um número: '))
    print('-=-'*30)
    j = input('Quer continuar?[S/N]').strip().lower()[0]
    c += 1
    soma += n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
print('Você digitou \033[32;40m {} \033[m números e a média entre eles foi \033[32;40m {:.3f} \033[m.'.format(c, soma/c))
print('O maior número digitado foi \033[34;40m {} \033[m e o menor \033[36;40m {} \033[m .'.format(maior, menor))

print(emoji.emojize(':sunglasses:'*10))
