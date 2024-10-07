import numpy as np
T = 5

matriz = np.zeros((T, T))
for i in range (0, 5):
    for j in range (0, 5):
        x = int(input(f'Digite um número para a posição [{j+1}][{i+1}]: '))
        matriz [j][i] = x
print(matriz)