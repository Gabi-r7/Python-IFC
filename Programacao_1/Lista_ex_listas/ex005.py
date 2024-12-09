# 5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. 
vetor = []
pares = []
impares = []

for i in range(20):
    vetor.append(int(input(f'Digite um número para a posição {i+1}°: ')))
    if vetor[i] % 2 == 0:
        pares.append(vetor[i])
    else:
        impares.append(vetor[i])
print(f'Vetor: {vetor}\nPares: {pares}\nImpares: {impares}')
