# Nessa atividade vamos criar um programa que informa o valor de um produto com X porcento de desconto

print('Caro funcionário esse programa calcula o valor final do produto de acordo com a porcetagem de desconto fornecido. \n Antes de conceder qualquer margem de desconto consulte seu gerente e solicite sua permissão.')
p = float(input('Informe o valor do produto: R$ '))
d = float(input('Informe a margem de desconto: '))
df = (p * d) / 100
pf = p - df
print(" O novo valor do produto será {:.2f} considerando o desconto concedito de {} %" .format(pf, d))

