# Faça uma sub-rotina que recebe duas listas A e B com dez
# elementos inteiros como parâmetro. A sub-rotina deverá determinar
# e mostrar o vetor C que contém os elementos que estão em A, mas
# que não estão em B. A lista C deverá ser mostrada no programa
# principal.

import random

A = set()
B = set()

for i in range(0, 10):
    A.add(random.randint(0, 15))
    B.add(random.randint(0, 15))

def mostrar(A, B):
    C = A - B
    print('C', C)

print('A:', A)
print('B:', B)
mostrar(A, B)