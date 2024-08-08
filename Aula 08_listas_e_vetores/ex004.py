# Faça um algoritmo que lê 5 valores para uma variável do tipo vetor e determine
# o maior e o menor valor armazenado no vetor
import numpy as np
N = 5
maior = 0
menor = 0
vetor = np.zeros(N)
for i in range(0, N):
    vetor[i] = int(input('Digite um número: '))
    if i == 0:
        maior = vetor[i]
        menor = vetor[i]
    else:
        if vetor[i] > maior:
            maior = vetor[i]
        if vetor[i] < menor:
            menor = vetor[i]
print(f'Maior: {maior}')
print(f'Menor: {menor}')