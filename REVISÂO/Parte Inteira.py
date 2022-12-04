# Crei programa que recebe um número qualquer e imprima o valor inteiro desse número

'''from math import trunc
n = float(input("Digite um número qualquer: "))
print("A parte inteira do número {} é {}" .format(n, trunc(n)))'''

import math
n = float(input("Digite um número: "))
print("A parte inteira do número {} é igual a {}" .format(n, math.trunc(n)))
