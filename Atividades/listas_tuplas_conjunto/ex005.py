# Faça um programa que preencha duas estruturas (lista, tupla ou conjunto), X e
# Y, com dez números inteiros cada. Calcule e mostre o seguinte resultado:
# A diferença entre X e Y, por exemplo:
import random
X = set()
Y = set()
for i in range(0, 10):
    X.add(random.randint(1, 100))
    Y.add(random.randint(1, 100))

print(f'Lista X: {X}\nLista Y: {Y}\n')
print(f'Diferença: {X - Y}')