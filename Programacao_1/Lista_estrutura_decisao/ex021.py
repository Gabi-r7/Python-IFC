# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
saque = float(input('Digite o valor a ser sacado: '))
saqueInicial = saque
quant_notas_1 = 0
quant_notas_5 = 0
quant_notas_10 = 0
quant_notas_50 = 0
quant_notas_100 = 0

if 10 < saque < 600:
    if saque >= 100:
        quant_notas_100 = saque // 100
    saque -= quant_notas_100 * 100
    if saque >= 50:
        quant_notas_50 = saque // 50
    saque -= quant_notas_50 * 50
    if saque >= 10:
        quant_notas_10 = saque // 10
    saque -= quant_notas_10 * 10
    if saque >= 5:
        quant_notas_5 = saque // 5
    saque -= quant_notas_5 * 5
    quant_notas_1 = saque

    print(f'Notas fornecidas para sacar R${saqueInicial:.2f}')
    print(f'{quant_notas_100} notas de 100')
    print(f'{quant_notas_50} notas de 50')
    print(f'{quant_notas_10} notas de 10')
    print(f'{quant_notas_5} notas de 5')
    print(f'{quant_notas_1} notas de 1')