data = input('Digite sua data de nascimento: ')
data = data.split('/')

if data[1] == '01':
    mes = 'Janeiro'
elif data[1] == '02':
    mes = 'Fevereiro'
elif data[1] == '03':
    mes = 'Março'
elif data[1] == '04':
    mes = 'Abril'
elif data[1] == '05':
    mes = 'Maio'
elif data[1] == '06':
    mes = 'Junho'
elif data[1] == '07':
    mes = 'Julho'
elif data[1] == '08':
    mes = 'Agosto'
elif data[1] == '09':
    mes = 'Setembro'
elif data[1] == '10':
    mes = 'Outubro'
elif data[1] == '11':
    mes = 'Novembro'
elif data[1] == '12':
    mes = 'Dezembro'
else:
    mes = 'Erro'
print(f'Você nasceu em {data[0]} de {mes} de {data[2]}')