# Nessa atividade temos de ciriar um programa de manipulação de strings onde temos  que realizar as seguintes tarefas:

#-  Informe seu nome completo:
#-Seu nome em maiúsculas é:
#- Seu nome e minúsculas é:
#- Seu nome tem ao todo ??? letras
#- Seu primeiro nome é ??? e tem ??? letras

nome = str(input("Digite seu nome completo: ")).strip()
dn = nome.split()
qt = ('').join(dn)
print("Analisando seu nome... ")
print("SEu nome em maiúsculas é: \033[36m{}\033[m" .format(nome.upper()))
print("Seu nome em minúsculas é: \033[1;32m{}\033[m" .format(nome.lower()))
#print("Seu nome tem ao total {} letras" .format(len(qt)))
print("Seu nome tem ao todo {} letras" .format(len(nome) - nome.count(" ")))
print("Seu primeiro nome é {} e ele tem {} letras" .format(dn[0] ,len(dn[0])))
#print("Seu primeiro nome tem {} letras" .format(nome.find(" ")))
