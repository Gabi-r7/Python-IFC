# Faça um algoritmo que lê 10 valores para uma variável do tipo vetor de nome x
# e mostra os 10 valores armazenados na estrutura.
import numpy as np
N = 10
x = np.zeros(N)
for i in range(0, 10):
    x[i] = int(input('Digite um número: '))
print(x)