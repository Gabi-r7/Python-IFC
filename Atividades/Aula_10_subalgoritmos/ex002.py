# Faça uma sub-rotina que receba como parâmetro uma matriz(lista
# de lista) A[5][5] e retorne a soma de todos os seus elementos.

import numpy as np

matriz = np.zeros((5, 5))


for i in range(0, 5):
    for j in range(0, 5):
        matriz[i][j] = np.random.randint(0, 10)

def soma(matriz):
    total = 0
    for i in range(0, 5):
        for j in range(0, 5):
            total += matriz[i][j]
    return total

total = soma(matriz)
print(f'Matriz:\n{matriz}')
print(f'Total: {total}')