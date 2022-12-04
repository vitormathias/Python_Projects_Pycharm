# Nessa atividade utilizaremos da biblioteca RANDON e criaremos um programa para realizar sorteios escolhendo númeor aleatórios

import random
print("Abaixo iremos realizar o sorteio das 6 dezenas para o sorteio do concurso 1000 da Mega Senna ")
n1 = random.randint(1, 60)
n2 = random.randint(1, 60)
n3 = random.randint(1, 60)
n4 = random.randint(1, 60)
n5 = random.randint(1, 60)
n6 = random.randint(1, 60)
print("Os números sorteados são {}, {}, {}, {}, {}, {}" .format(n1, n2, n3,n4,n5, n6))

