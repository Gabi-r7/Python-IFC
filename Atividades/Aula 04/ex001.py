# Faça um programa que receba três notas, calcule e mostre a médias ponderadas 
# dessas notas, considerando peso 3 para a primeira nota, peso 2 para a segunda nota e 
# peso 5 para a terceira nota. Imprima aprovado de a média for maior ou igual a 6 e 
# reprovado se for menor

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = ((n1*3) + (n2*2) + (n3*5)) / (3+2+5)

if media >= 6:
    print(f'Aprovado! Sua média foi de {media:.2f}!')
elif media < 6:
    print(f'Reprovado! Sua média foi de {media:.2f}!')
else:
    print('Erro!')