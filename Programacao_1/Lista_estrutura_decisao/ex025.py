# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
quant_sim = 0
op = 0

print('O quão suspeito você é?')
print('A cada pergunta, digite 1 para sim e 0 para não')
op += int(input('Telefonou para a vítima: '))
op += int(input('Esteve no local do crime: '))
op += int(input('Mora perto da vítima: '))
op += int(input('Devia para a vítima: '))
op += int(input('Já trabalhou com a vítima: '))
if op < 2:
    print('Inocente')
elif op == 2:
    print('Suspeita')
elif 3 >= op <= 4:
    print('Cúmplice')
else:
    print('Assassino')