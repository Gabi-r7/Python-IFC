idade = int(input('Digite sua idade: '))
sexo = input('Digite seu sexo (M/F): ')

if sexo == 'F':
    if idade >= 0 and idade <= 12:
        print('Menina!')
    elif idade > 12 and idade <= 24:
        print('Moça!')
    elif idade > 24:
        print('Mulher!')
    else:
        print('Erro! Idade inválida')
elif sexo == 'M':
    if idade >= 0 and idade <= 12:
        print('Menino!')
    elif idade > 12 and idade <= 24:
        print('Rapaz!')
    elif idade > 24:
        print('Homem!')
    else:
        print('Erro! Idade inválida')
else:
    print('Erro! Sexo inválido')
 