x = float(input('Digite um valor para x: '))
y = float(input('Digite um valor para y: '))

if 0.3 * (x + y) > 500:
    aux = x
    x = y
    y = aux
    print(f'Valores trocados! X: {x:.2f}, Y: {y:.2f}')
else:
    if x < y:
        print(f'Menor valor: {x:.2f}')
    else:
        print(f'Menor valor: {y:.2f}')
