print('{:=^40}'.format('Lojas Guanabara'))
preco = float(input('Qual o valor do produto?'))
pagamento = input('Qual o meio de pagamento').lower()

if pagamento == 'dinheiro':
    print('Você tem direito a 10% de desconto e pagará R${}'.format(0.9*preco))
if pagamento == 'cartão':
    parcelas = int(input('Em quantas parcelas?'))
    if parcelas == 1:
        print('O valor pago será de R${}'.format(0.95*preco))
    elif parcelas == 2:
        print('O valor pago será de R${}'.format(preco))
    else:
        print('O valor pago será de R${}'.format(1.2*preco))
print('Como é bom receber um aumento')
