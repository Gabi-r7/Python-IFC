# Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = n1
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')