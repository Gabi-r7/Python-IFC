# 13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ). 
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = []
media_anual_temperaturas = 0

for i in range(12):
    temperaturas.append(float(input(f'Digite a temperatura média mensal para o mês de {meses[i]}: ')))
    media_anual_temperaturas += temperaturas[i]
media_anual_temperaturas /= len(temperaturas)
print(f'Média anual de {media_anual_temperaturas:.2f}°C')

print(f'Temperaturas acima da média anual:')
for i in range(12):
    if temperaturas[i] > media_anual_temperaturas:
        print(f'{temperaturas[i]:.2f}°C no mês de {meses[i]}')
