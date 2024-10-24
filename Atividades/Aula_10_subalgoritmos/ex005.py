# Construa uma função que receba como parâmetro uma matriz
# quadrada 4 X 4 e retorne a soma dos valores da diagonal
# principal.

import numpy as np

matriz = np.zeros((4, 4))
for i in range(0, 4):
    for j in range(0, 4):
        matriz[i][j] = np.random.randint(0, 50)

def soma(matriz):
    total = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if i == j:
                total += matriz[i][j]
    return total    
total = soma(matriz)
print(f'Matriz:\n{matriz}')
print(f'Total diagonal soma principal: {total}')