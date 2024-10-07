dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
invalido = False
bissexto = False

if ano < 0:
    invalido = True
if mes == 2 and ano % 4 == 0:
    if dia > 29 or dia < 1:
        invalido = True
elif mes == 2:
    if dia > 28 or dia < 1:
        invalido = True
if mes < 1 or mes > 12:
    invalido = True
if mes == 1 or mes == 5 or mes == 7 or mes == 8 or mes == 12 or mes == 3 or mes == 10:
    if dia > 31 or dia < 1:
        invalido = True
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 30 or dia < 1:
        invalido = True

if invalido:
    print('Data inválida!')
else:
    print('Data válida!')