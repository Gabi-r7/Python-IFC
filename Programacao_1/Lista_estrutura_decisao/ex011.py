# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa 
# que deve calcular os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario_inicial = float(input('Digite o salário inicial: '))
reajuste = 0
if salario_inicial <= 280 and salario_inicial > 0:
    reajuste = 0.20
elif salario_inicial > 280 and salario_inicial <= 700:
    reajuste = 0.15
elif salario_inicial > 700 and salario_inicial <= 1500:
    reajuste = 0.10
elif salario_inicial > 1500:
    reajuste = 0.05
else:
    print('Salário inválido')

salario_reajustado = salario_inicial + (salario_inicial * reajuste)
print(f'Salário inicial: R${salario_inicial:.2f}')
print(f'Percentual de aumento: {reajuste * 100:.2f}%')
print(f'Valor do aumento: R${salario_reajustado - salario_inicial:.2f}')
print(f'Novo salário: R${salario_reajustado:.2f}')