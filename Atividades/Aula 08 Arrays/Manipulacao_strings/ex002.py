# Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando 
# apenas letras maiúsculas. 

nome = input('Digite seu nome: ')
for i in range(len(nome)):
    print(nome[:i+1].upper())