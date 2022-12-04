
"""print('\033[1;33m-----------------------------------------')
print("\033[1;34mVou pensar em um número entre 0 e 5...")
print('\033[1;33m-----------------------------------------')"""


nome = str(input("Digite seu primeiro nome: ")).strip().title()
if nome == "João":
    print("Parabéns estavamos procurando um \033[1;33mJoão")
else:
    print("\033[1;31mQue pena esse não é o nome que buscamos")