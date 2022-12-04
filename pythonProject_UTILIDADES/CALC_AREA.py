from math import ceil
largura = float(input('Digite a largura: '))
comprimento = float(input('Digite a altura: '))
area = ceil(largura * comprimento)
areat = ceil(area + (area * 10 / 100))
print('A área dessa parede é {} mm²'.format(area))
print('A seguir você pode digitar os valores em centimetros que faremos a conversão para m²')
valor = float(input('Insira o valor de cada caixa de:' ))
alargura = float(input('Insira a medida da largura do acabamento desejado: '))
acomprimento = float(input('Insira o comprimento do acabamento desejado: '))
aarea = (alargura / 100) * (acomprimento / 100)
npecas = ceil(areat / aarea)
ncaixas = ceil(areat * 1)
custo = (ncaixas * valor)
print('Para cobrir a sua parede que tem {} m² .Considerando a mrgem de 10% de recortes serãão necessários {} peças de acabamento, ou seja {} caixas'.format(area, npecas , ncaixas))
print("Seu custo total nas {} caixas será de R$ {} ".format(ncaixas, custo))





# Não esquecer de considerar a  margem de 10% de recortes



