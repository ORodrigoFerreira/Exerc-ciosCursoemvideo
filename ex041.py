idade = int(input('Qual a idade do atleta?'))

if idade <= 9:
    print('A sua categoria é \033[1;31;40m MIRIM \033[m')
elif idade <= 14:
    print('A sua categoria é \033[1;32;40m INFANTIL \033[m')
elif idade <= 19:
    print('A sua categoria é \033[1;33;40m JUNIOR \033[m')
elif idade <= 20:
    print('A sua categoria é \033[1;34;40m SÊNIOR \033[m')
else:
    print('A sua categoria é \033[1;36;40m MASTER \033[m')
