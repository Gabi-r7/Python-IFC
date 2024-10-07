a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
c = int(input('Digite um valor para C: '))
d = int(input('Digite um valor para D: '))
e = int(input('Digite um valor para E: '))

if a > b and a > c and a > d and a > e:
    print(f'O maior valor é {a}!')
elif b > a and b > c and b > d and b > e:
    print(f'O maior valor é {b}!')
elif c > a and c > b and c > d and c > e:
    print(f'O maior valor é {c}!')
elif d > a and d > b and d > c and d > e:
    print(f'O maior valor é {d}!')
elif e > a and e > b and e > c and e > a:
    print(f'O maior valor é {e}!')
else:
    print('Erro!')