
nome = str(input("Digite seu nome completo: ")).strip()
n = nome.split()
print("Seu primeiro nome é: \033[0;33m{}\033[m".format(n[0]))
print("Seu último nome é: \033[1;33m{}\033[m" .format(n[len(n)-1]))
