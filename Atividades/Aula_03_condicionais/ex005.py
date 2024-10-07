litros = float(input('Digite a quantidade de litros vendidos: '))
tipo = input('Digite o tipo de combustível (A = Álcool|G = Gasolina): ')

if tipo == 'A':
    if litros < 20:
        total = ((6.50 * 0.97) * litros)
    elif litros >= 20:
        total = ((6.50 * 0.95)* litros)
    else:
        print('Erro! Quantidade inválida!')
elif tipo == 'G':
    if litros < 20:
        total = ((7.20 * 0.96)* litros)
    elif litros >= 20:
        total = ((7.20 * 0.94)* litros)
    else:
        print('Erro! Quantidade inválida!')
else:
    print('Erro! Tipo inválido!')
print(f'O valor a ser pago é de R${total:.2f}')