import numpy as np

principal = 0
soma = 0
matriz = np.zeros((10, 10))
for i in range (0, 10):
    for j in range (0, 10):
        x = int(input(f'Digite um número para a posição [{i+1}][{j+1}]: '))
        matriz [i][j] = x
        if i == j:
            principal += x
        if i == 2:
            soma += x
print(matriz)
print(f'principal: {principal}')
print(f'soma: {soma}')