# Nessa atividade criaremos um programa para calcular a  raiz quadrada utilizando módulo MATH

from math import sqrt, ceil
print("Olá vou te ajudar  a  calcular a  raiz quadrada dos número.")
n = int(input(" Digite o número o qual vocÊ quer sber o valor da raiz quadrada: "))
print("A raiz quadrada de {} é igual a {}" .format(n, ceil(sqrt(n))))