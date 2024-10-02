import numpy as np
T = 5

principal = []
matriz = np.zeros((T, T))
for i in range (0, 5):
    for j in range (0, 5):
        x = int(input(f'Digite um número para a posição [{i+1}][{j+1}]: '))
        matriz [i][j] = x
        if i == j:
            principal.append(matriz[i][j])
print(principal)