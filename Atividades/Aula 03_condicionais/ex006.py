dia = int(input('Digite os dias: '))
mes = int(input('Digite os meses: '))
ano = int(input('Digite os anos: '))
diasS = int(input('Digite quantos dias quer somar: '))

if diasS > 365:
    anosAMais = round(diasS / 365)  #adiciona aos anos a quantidade a mais e arredonda
    ano += anosAMais
    diasS -= anosAMais * 365
elif diasS > 30:
    mesesAMais = round(diasS / 30)
    mes += mesesAMais
    diasS -= mesesAMais * 30
elif diasS > 0:
    dia += diasS
    # if dia > 30:
    #     mes += 1
    #     dia

print(f'dia: {dia}\n mes: {mes}\n ano: {ano}')
