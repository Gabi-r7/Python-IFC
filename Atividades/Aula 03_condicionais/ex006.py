dia = int(input('Digite os dias: '))
mes = int(input('Digite os meses: '))
ano = int(input('Digite os anos: '))
diasS = int(input('Digite quantos dias quer somar: '))

diasS += dia
dia = 0
if diasS > 365:
    anosAMais = diasS // 365  #adiciona aos anos a quantidade a mais e arredonda
    ano += anosAMais
    diasS -= anosAMais * 365
if diasS > 30:
    mesesAMais = diasS // 30
    mes += mesesAMais
    diasS -= mesesAMais * 30
if diasS > 0:
    dia += diasS
    
print(f'dia: {dia}\n mes: {mes}\n ano: {ano}')