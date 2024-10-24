# Crie uma sub-rotina que receba como parâmetro um vetor V[15] de
# números inteiros e substitua todos os valores negativos de A por 0. O
# vetor deverá ser mostrado no programa principal.

import numpy as np

V = np.zeros(15)
for i in range(0, 15):
    V[i] = np.random.randint(-50, 50)
print(f'Vetor:\n{V}')

def substitui(vetor):
    for i in range(0, len(V)):
        if V[i] < 0:
            V[i] = 0
    return vetor
V = substitui(V)
print(f'Substituido:\n{V}')