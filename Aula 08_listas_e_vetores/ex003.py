# Faça um algoritmo que lê 5 valores para uma variável do tipo vetor e determine
# a média de todos os valores armazenados no vetor
import numpy as np
N = 5
vetor = np.zeros(N)
media = 0
for i in range(0, N):
    vetor[i] = int(input('Digite um número: '))
    media += vetor[i]
media /= N
print(f'Média: {media:.2f}')