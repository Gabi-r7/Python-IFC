# Escreva um algoritmo que receba cinco números do usuário e imprima o cubo de cada número
x = 1
while x <= 5:
    n = float(input(f'Escreva o {x}° número: '))
    print(f'{n ** 3}')
    x += 1