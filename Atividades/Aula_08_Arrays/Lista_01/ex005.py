# Faça um algoritmo que lê duas listas A e B com 5 elementos cada. Construir uma 
# lista C, sendo este a junção das duas outras listas, ou seja, a lista C deverá conter 
# 10 elementos. Mostre no final a lista C.

A = []
B = []
C = []

for i in range(5):
    A.append(int(input(f'Digite o {i+1}º valor da lista A: ')))

for i in range(5):
    B.append(int(input(f'Digite o {i+1}º valor da lista B: ')))

C = A + B
print(C)