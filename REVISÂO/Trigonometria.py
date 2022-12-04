# Crie programa que dado o angulo ele informa o SEno, Cosceno e Tangente do angulo.


from math import radians, sin, cos, tan
a = float(input("Digite o ângulo desejado: "))
print('O SENO do ângulo {} é igual a {:.2f}' .format(a, sin(radians(a))))
print("O COSCENO do ângulo {} é igual a {:.2f}" .format(a, cos(radians(a))))
print("A TANGENTE do ângulo {} é igual a {:.2f}" .format(a, tan(radians(a))))

