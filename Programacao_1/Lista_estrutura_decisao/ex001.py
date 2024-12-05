# Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
maior = n1
if n2 > maior:
    maior = n2
print(f'O maior número é: {maior}')