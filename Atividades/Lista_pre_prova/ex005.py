import numpy as np

matriz = np.zeros((3, 3))
soma = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input('Digite um valor: '))
        soma += matriz[i][j]
print(f'Matriz:\n {matriz}')
print(f'Soma: {soma}')
