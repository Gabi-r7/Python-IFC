# Faça um algoritmo que lê 10 valores para uma variável do tipo vetor e mostre
# qual a posição está armazenado o maior e o menor valor no vetor
import numpy as np
N = 10
vetor = np.zeros(N)
maiorPosicao = 0
menorPosicao = 0
for i in range(0, N):
    vetor[i] = int(input('Digite um número: '))
    if vetor[i] > vetor[maiorPosicao]:
        maiorPosicao = i
    if vetor[i] < vetor[menorPosicao]:
        menorPosicao = i
print(f'Maior valor: {vetor[maiorPosicao]} na posição {maiorPosicao}')
print(f'Menor valor: {vetor[menorPosicao]} na posição {menorPosicao}')