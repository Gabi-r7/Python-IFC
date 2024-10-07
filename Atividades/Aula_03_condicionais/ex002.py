a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
c = int(input('Digite um valor para C: '))

if a < b and a < c:
    if b < c:
        print(f'{a}, {b}, {c}')
    else:
        print(f'{a}, {c}, {b}')
elif b < a and b < c:
    if a < c:
        print(f'{b}, {a}, {c}')
    else:
        print(f'{b}, {c}, {a}')
elif c < a and c < b:
    if a < b:
        print(f'{c}, {a}, {b}')
    else:
        print(f'{c}, {b}, {a}')
else:
    print('Erro!')
