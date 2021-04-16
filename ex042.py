a = float(input('Primeiro lado'))
b = float(input('Segundo Número'))
c = float(input('Terceiro número'))

if a < b+c and b < c + a and c < a + b:
    print('Com esses valores é possível formar um triângulo.')
    if a != b != c:
        print('E a classificação desse triângulo é \033[32;40m ESCALENO \033[m.')
    elif a == b == c:
        print('E a classificação desse triângulo é \033[31;40mEQUILÁTERO\033[m.')
    elif b == c or a == b or a == c:
        print('E a classificação desse triângulo é \033[33;40m ISÓSCELES \033[m.')
else:
    print('Esses valores não formam um triângulo.')