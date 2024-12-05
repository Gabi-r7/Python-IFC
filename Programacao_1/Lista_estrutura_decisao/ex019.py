# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
num = int(input('Digite um número: '))
numInicial = num

centenas = 0
dezenas = 0
unidades = 0

if 0 < num < 1000:
    centenas = num // 100
    num = num % 100
    dezenas = num // 10
    num = num % 10
    unidades = num

    print(f'{numInicial} = ', end='')
    print(f'{centenas} centena', end='')
    if centenas != 1:
        print('s', end='')
    print(', ', end='')

    print(f'{dezenas} dezena', end='')
    if dezenas != 1:
        print('s', end='')
    print(' e ', end='')

    print(f'{unidades} unidade', end='')
    if unidades != 1:
        print('s', end='')
else:
    print('Número inválido')