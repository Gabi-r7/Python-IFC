dia = int(input('Digite os dias: '))
mes = int(input('Digite os meses: '))
ano = int(input('Digite os anos: '))
diasS = int(input('Digite quantos dias quer somar: '))


anosAMais = round(diasS / 365)  #adiciona aos anos a quantidade a mais e arredonda
ano += anosAMais
diasS -= anosAMais * 365
mesesAMais = round(diasS / 30)
mes += mesesAMais
diasS -= mesesAMais * 30
dia += diasS

print(f'dia: {dia}\n mes: {mes}\n ano: {ano}')















# dia += diasS
# if dia > 30: 
#     aux = dia #auxiliar recebe dia
#     aux -= 30 #auxiliar tira o valor de um mes e fica com a diferença
#     dia -= aux #a diferença é retirada do dia, dia = 30
#     mes += (aux / 30)
