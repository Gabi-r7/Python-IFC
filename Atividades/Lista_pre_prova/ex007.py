import numpy as np

lixta = np.zeros(10)
for i in range(0, len(lixta)):
    lixta[i] = int(input('Mim de um número: '))
conjunto = set(lixta)
print(f'Lista: {lixta}')
print(f'Conjunto: {conjunto}')