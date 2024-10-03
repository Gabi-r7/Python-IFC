import numpy as np

lista = np.zeros(5)
for i in range(0, 5):
    lista[i] = int(input('Digite um número: '))

maior = lista[0]
menor = lista[0]
for i in range(0, 5):
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
print(lista)
print(f'maior: {maior}')
print(f'menor: {menor}')