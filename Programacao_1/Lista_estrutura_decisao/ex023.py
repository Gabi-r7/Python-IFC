# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
num = float(input('Digite um número qualquer: '))
if num.is_integer():
    print('Número é inteiro')
else:
    print('Número é decimal')