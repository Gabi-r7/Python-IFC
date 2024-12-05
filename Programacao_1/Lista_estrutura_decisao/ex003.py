# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
# F - Feminino, M - Masculino, Sexo Inválido.
sex = input('Digite seu sexo ("F" para feminino ou "M" para masculino): ').upper()
if sex == 'M':
    print('Seu sexo é masculino')
elif sex == 'F':
    print('Seu sexo é feminino')
else:
    print('Sexo inválido')