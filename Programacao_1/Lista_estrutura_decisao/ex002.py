# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
n1 = int(input('Digite o primeiro número: '))
if n1 < 0:
    print(f'{n1} é negativo')
elif n1 > 0:
    print(f'{n1} é positivo')
else:
    print(f'{n1} é nulo')