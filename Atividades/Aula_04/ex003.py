# Faça um programa que pergunte o preço de três produtos e informe qual produto 
# você deve comprar, sabendo que a decisão é sempre o mais barato.   

p1 = float(input('Digite o primeiro preço: '))
p2 = float(input('Digite o segundo preço: '))
p3 = float(input('Digite o terceiro preço: '))

menor = p1
if p2 < menor:
    menor = p2
if p3 < menor:
    menor = p3
print(f'Compre o do preço R${menor:.2f}')