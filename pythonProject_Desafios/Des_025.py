#Criar programa que lê um nome e verifica se o nome tem SILVA

nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome tem Silva ?  {}" .format("SILVA" in nome.upper()))