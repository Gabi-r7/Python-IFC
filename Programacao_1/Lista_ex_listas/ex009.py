# 9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor. 
a = []
quadrados = []

for i in range(10):
    a.append(int(input('Digite um número inteiro: ')))
    quadrados.append(a[i]**2)
print(f'A: {a}')
print(f'Quadrados: {quadrados}')
print(f'Soma dos quadrados: {sum(quadrados)}')
