# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça: 
# a. Mostre a quantidade de valores que foram lidos; 
# b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro; 
# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; 
# d. Calcule e mostre a soma dos valores; 
# e. Calcule e mostre a média dos valores; 
# f. Calcule e mostre a quantidade de valores acima da média calculada; 
# g. Calcule e mostre a quantidade de valores abaixo de sete; 
# h. Encerre o programa com uma mensagem; 
notas = []
media_notas = 0
soma_notas = 0
quant_notas = 0
quant_notas_acima_media = 0
quant_notas_abaixo_sete = 0
valor = 0

while valor != -1:
    valor = float(input('Digite um valor para uma nota: '))
    if valor == -1:
        break
    else:
        notas.append(valor)
        soma_notas += notas[quant_notas]
        quant_notas += 1

media_notas = soma_notas / quant_notas

print(f'Quantidade de valores informados: {quant_notas}')

print(f'Notas: {notas}') #b

print('Notas na ordem inversa:') #c
for nota in notas[::-1]:
    print(nota)

print(f'Soma das notas: {soma_notas:.2f}') #d

print(f'Média das notas: {media_notas:.2f}') #e

print('Notas acima da média: ', end='') #f
for nota in notas:
    if nota > media_notas:
        quant_notas_acima_media += 1
    if nota < 7:
        quant_notas_abaixo_sete += 1
        
print(quant_notas_acima_media)

print(f'Notas abaixo de 7: {quant_notas_abaixo_sete}') #g

print('Até mais!')
