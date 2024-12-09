# 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela. 
notas = []
media = 0

for i in range(4):
    notas.append(float(input(f'Digite a {i+1}° nota: ')))
    media += notas[i]
media /= len(notas)
print(f'Notas: {notas}')
print(f'Média: {media}')
