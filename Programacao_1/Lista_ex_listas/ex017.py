#  Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo: 
# Atleta: Rodrigo Curvêllo 
# Primeiro Salto: 6.5 m 
# Segundo Salto: 6.1 m 
# Terceiro Salto: 6.2 m 
# Quarto Salto: 5.4 m 
# Quinto Salto: 5.3 m 
# Resultado final: 
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3 
# Média dos saltos: 5.9 m 

saltos = []
media_saltos = 0

while True:
    nome_atleta = input('Digite o nome do atleta: ')

    if nome_atleta == '':
        break

    for i in range(5):
        saltos.append(float(input(f'Digite a distância do {i+1}° salto: ')))
        media_saltos += saltos[i]

    media_saltos /= len(saltos)
    print('Resultado Final')
    print(f'Atleta: {nome_atleta}')
    print(f'Saltos: {saltos}')
    print(f'Média dos saltos: {media_saltos} m')

    saltos = []
    media_saltos = 0
