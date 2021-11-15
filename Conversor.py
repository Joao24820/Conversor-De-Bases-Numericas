import math

n1 = int(input('Digite um numero inteiro: '))
print('[1] para binario ''\n[2]para octal''\n[3] para hexadecimal')
es = int(input('Escolha um dos numeros:'))

if es == 1:
    b = bin(n1)[2:]
    print('O numero {} em binario é {}'.format(n1, b))

elif es == 2:
    o = oct(n1)[2:]
    print('O numero {} em octal é {}'.format(n1, o))

elif es == 3:
    h = hex(n1)[2:]
    print('O numero {} em hexadecimal é {}'.format(n1, h))

elif es >= 4:
    print('OPÇÃO INVALIDA')
