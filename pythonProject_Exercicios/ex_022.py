#"""" Desafio 22 - Crie um programa que leia o nome completo de uma pessoa  e mpstre:

#1 - O nome com todas as letras  MAIUSCULAS
#2 - O nome com todas as letras  minusculas
#3 - Quantidade de letras total ( Sem considerar os espaços)
#4 - Quantas letras tem o primeiro nome



nome = str(input('Digite seu nome completo '))
print(nome.upper())
print(nome.lower())
print(nome.title())
div = nome.split()
print('Seu nome completo possui {} letras ao total'.format(len(nome.strip())))
print(len(div[0]))




