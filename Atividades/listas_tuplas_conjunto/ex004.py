# Faça um programa que preencha uma estrutura (lista, tupla ou conjunto) com 9
# números inteiros, calcule e mostre os números primos e suas respectivas
# posições na estrutura
import random
Sla = []
for i in range(9):
    Sla.append(random.randint(1, 100))
print(f'A lista gerada foi: {Sla}\n')

podePrimo = False
for i in range(9):
    if Sla[i] > 1:
        podePrimo = True
        for j in range (2, int(Sla[i] ** 0.5) + 1):
            if Sla[i] % j == 0:
                podePrimo = False
                break
        if podePrimo:
            print(f'O número {Sla[i]} é primo e está na posição {i} da lista.')