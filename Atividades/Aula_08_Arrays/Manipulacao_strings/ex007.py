str1 = input('Digite a primeira estringue: ')
str2 = input('Digite a segunda estringue: ')
achax = str1.find(str2)
if achax != -1:
    print(f'Achou {str2} na posição: {achax}')
else:
    print('Não encontrado')