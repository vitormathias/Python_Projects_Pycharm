# Nessa atividade vamos criar um programa que informa o valor de um produto com X porcento de desconto

print("Olá caro cliente seja bem vindo aos mercados Bom Preço  ! ")
p = float(input("Consederemos  desconto de 5%.  Informe o valor do produto: R$ "))
d = (p * 5) / 100
print("O valor do produto original é {} , considerando o desconto de 5% equivalente a {} , o valor final do seu produto será {}".format(p, d, (p - d)))

