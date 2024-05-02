# Escreva um algoritmo que leia dez números do usuário e imprima a metade de cada número
x = 1
while x <= 10:
    n = float(input(f'Escreva o {x}° número: '))
    print(f'{x / 2}')
    x += 1