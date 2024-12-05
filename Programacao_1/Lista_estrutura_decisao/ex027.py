# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                   Até 5 Kg                Acima de 5 Kg
# Morango           R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã              R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.
quant_maca_kg = float(input('Digite a quantidade de maçãs compradas (em Kg): '))
quant_morango_kg = float(input('Digite a quantidade de morango comprado (em Kg): '))
preco_total = 0

if quant_maca_kg < 5:
    preco_total += quant_maca_kg * 2.50
else:
    preco_total += quant_maca_kg * 2.20

if quant_morango_kg < 5:
    preco_total += quant_morango_kg * 1.80
else:
    preco_total += quant_morango_kg * 1.50

if quant_morango_kg + quant_maca_kg > 8 or preco_total > 25:
    preco_total -= preco_total * 0.10

print(f'O cliente pagará um total de R${preco_total:.2f} por:\n{quant_maca_kg:.2f}Kg de maçã\n{quant_morango_kg:.2f}Kg de morango')