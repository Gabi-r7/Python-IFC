n = int(input('Digite um número: '))
total = n
for i in range(1, n):
    total *= i
    print(f'{n} x {i} = {total}')
print(f'O fatorial de {n} é {total}')