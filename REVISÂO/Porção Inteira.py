# Faça um programa onde é solicitado um número e seja dada a parte inteira desse número

from math import trunc
print("Digite um número qualquer: ")
n = float(input("Digite um número qualquer"))
print("A parte inteira do número {} é {}" .format(n, trunc(n)))