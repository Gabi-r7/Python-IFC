import numpy as np

soma = 0
matriz = np.zeros((5, 5))
for i in range (0, 5):
    for j in range (0, 5):
        x = int(input(f'Digite um número para a posição [{i+1}][{j+1}]: '))
        matriz [i][j] = x
        if i == 4:
            soma += x
print(matriz)
print (soma)