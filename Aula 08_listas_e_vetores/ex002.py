# Faça um algoritmo que lê 5 valores para uma variável do tipo vetor e determine
# o somatório de todos os valores armazenados no vetor.
import numpy as np
N = 5
vetor = np.zeros(N)
soma = 0
for i in range(0, N):
    vetor[i] = int(input('Digite um número: '))
    soma += vetor[i]
print(f'Soma: {soma:.2f}')