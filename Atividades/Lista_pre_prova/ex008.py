import numpy as np

matrix = np.zeros((2, 2))
lixta = []
for i in range(0, 2):
    for j in range(0, 2):
        matrix[i][j] = float(input('Digite um número: '))
        if i == j:
            lixta.append(matrix[i][j])
print(f'Matriz digitada:\n{matrix}')
print(f'Diagonal principal: {lixta}')