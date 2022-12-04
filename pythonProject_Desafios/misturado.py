

print("Venha conhecer nosso programa revolucionário.")
nome = str(input("Informe seu nome completo: ")).strip().upper()
print("Aguarde enquanto vamos analisar seu nome...\2Pronto !!! Abaixo segue o resultado da análise:")
print("Seu nome completo em maiúsculo é: \033[1;36m{}\033[m" .format(nome.upper()))
print("Seu nome em minúsculas é: \033[1;31m{}\033[m" .format(nome.lower()))
print("Seu nome completo tem \033[1;32m{}\033[m" .format(len(nome) - nome.count(" ")))
n = nome.split()
print("Seu primeiro nome é \033[1;33m{}\033[m e ele tem \033[1;32m{}\033[m letras" .format(n[0] ,len(n[0])))
print("Seu nome do meio é \033[1;33m{}\033[m e tem \033[1;32m{}\033[m letras." .format(n[len(n) - 2] ,len(n[len(n) - 2])))
print("Seu último nome é \033[1;33m{}\033[m e ele tem \033[1;32m{}\033[m letras." .format(n[len(n) - 1] ,len(n[len(n) - 1])))
