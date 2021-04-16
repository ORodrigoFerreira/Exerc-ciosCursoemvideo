peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura'))
imc = peso/(altura**2)

if imc <= 18.5:
    print('Você está abaixo do peso ideal! Coma mais e procure o nutricionista.')
elif imc <= 25:
    print('Você está no peso ideal, mantenha assim!')
elif imc <= 30:
    print('Você está em Sobrepeso. Melhore a sua alimentação e faça exercício físico.')
elif imc <= 40:
    print('Você está OBESO. Procure ajuda e tenha hábitos mais saudáveis.')
elif imc > 40:
    print('Você está em OBESIDADE MÓRBIDA. PROCURE AJUDA IMEDIATAMENTE.')
