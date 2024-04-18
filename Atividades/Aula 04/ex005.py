# Faça um programa que receba o código correspondente ao cargo de um funcionário e 
# seu salário atual e mostre o cargo, o valor do aumento e seu novo salário. Os cargos 
# estão na tabela a seguir: 

codigo = int(input('Digite seu código: '))
salario = float(input('Digite seu salário: '))

if codigo > 5 or codigo < 1:
    print('Código inválido!')
elif codigo == 1:
    cargo = 'Escriturário'
    aumento = '50%'
    nsalario = (salario * 0.50) + salario
    print(f'Seu cargo é {cargo}! Seu aumento é de R${nsalario - salario:.2f}! Seu novo salário é de R${nsalario:.2f}')
elif codigo == 2:
    cargo = 'Secretário'
    aumento = '35%'
    nsalario = (salario * 0.35) + salario
    print(f'Seu cargo é {cargo}! Seu aumento é de R${nsalario - salario:.2f}! Seu novo salário é de R${nsalario:.2f}')
elif codigo == 3:
    cargo = 'Caixa'
    aumento = '20%'
    nsalario = (salario * 0.20) + salario
    print(f'Seu cargo é {cargo}! Seu aumento é de R${nsalario - salario:.2f}! Seu novo salário é de R${nsalario:.2f}')
elif codigo == 4:
    cargo = 'Gerente'
    aumento = '10%'
    nsalario = (salario * 0.10) + salario
    print(f'Seu cargo é {cargo}! Seu aumento é de R${nsalario - salario:.2f}! Seu novo salário é de R${nsalario:.2f}')
elif codigo == 5:
    cargo = 'Diretor'
    aumento = '0%'
    print(f'Você não terá aumento')
