

"""nome = str(input("Informe seu nome: "))
print("Seu noma começa com Santo ?  {}" .format(nome[:5].upper() == "SILVA"))"""

"""nome = str(input("Informe seu nome: ")).strip()
print("O seu nome tem Silva ?  {}" .format("SILVA" in nome.upper()))"""

frase = str(input("Digite uma frase qualquer: ")).strip().upper()
print("A letra A aparece {} vezes na frase" .format(frase.count("A")))
print("A primeira letra A aparece na posição {}".format(frase.find("A")+1))
print("A última letra A aparece na posição {}".format(frase.rfind("A")+1))