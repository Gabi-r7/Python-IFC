# Faça um programa que receba o ano de nascimento de uma pessoa, calcule e mostre: 
# a. Se ele já tem idade para votar (16 anos ou mais);

ano = int(input('Digite seu ano de nascimento: '))
idade = 2024 - ano
if idade >= 16:
    print('Você pode votar!')
elif idade < 16:
    print('Você não pode votar!')
else:
    print('Erro!')