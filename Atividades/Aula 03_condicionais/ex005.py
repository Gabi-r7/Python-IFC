litros = float(input('Digite a quantidade de litros vendidos: '))
tipo = input('Digite o tipo de combustível (A = Álcool|G = Gasolina): ')

if tipo == 'A':
    if litros < 20:
        total = (6.50 * litros) - (litros * 0.03)
    elif litros >= 20:
        total = (6.50 * litros) - (litros * 0.05)
    else:
        print('Erro! Quantidade inválida!')
elif tipo == 'G':
    if litros < 20:
        total = (7.20 * litros) - (litros * 0.04)
    elif litros >= 20:
        total = (7.20 * litros) - (litros * 0.06)
    else:
        print('Erro! Quantidade inválida!')
else:
    print('Erro! Tipo inválido!')
print(f'O valor a ser pago é de R${total:.2f}')