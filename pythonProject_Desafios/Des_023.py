#?Nessa atividade temos que criar um programa que lerá um número e  o separará em milhares, centenas, dezenas e milhar

num = int(input('Digite um número: '))
n = str(num)
print("Analisando o número {}" .format(n))
print("Unidade:  {}" .format(n[3]))
print("Dezena:  {:>2}" .format(n[2]))
print("Centena:  {}" .format(n[1]))
print("Milhar: {:>3}" .format(n[0]))
