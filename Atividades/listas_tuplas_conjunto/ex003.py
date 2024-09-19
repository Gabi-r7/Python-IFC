# Faça um algoritmo que lê estrutura (lista, tupla ou conjunto), K que comporte 20
# elementos. Troque a seguir os elementos de índice ímpar com os de índice par 
# imediatamente seguinte mostre no final como ficou a estrutura K, com as alterações.
K = []
impares = []
pares = []
for i in range(20):
    K.append(int(input('Digite um número para a lista K: ')))

for i in range(0, 20, 2):
    pares.append(K[i])
    impares.append(K[i+1])

for i in range(0, 20, 2):
    K[i] = impares[i//2]
    K[i+1] = pares[i//2]
print(K)