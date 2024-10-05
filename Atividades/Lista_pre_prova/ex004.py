import numpy as np

array = np.zeros(6)
contrario = np.zeros(6)
for i in range(0, 6):
    array[i] = int(input('Digite um número: '))

print(f'Foi inserido: {array}')

for i in range(0, 6):
    contrario[i] = array[(len(array)-1) - i]
print(f'Contrário: {contrario}')