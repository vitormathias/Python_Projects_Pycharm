# Criar programa que leia peso e  altura e  informe o IMC do usuário

from math import trunc
peso = float(input('Informe seu peso '))
altura = float(input('Informe sua altura '))
imc = trunc(peso / altura ** 2)
print('Você pesa {} Kg e mede {} m o seu IMC é {} '.format(peso, altura, imc))


