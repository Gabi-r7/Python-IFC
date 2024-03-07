total = float(input('Digite seu depósito: '))
total -= (total * 0.0038) + float(input('Digite o valor do primeiro saque: '))
total -= (total * 0.0038) + float(input('Digite o valor do segundo saque: '))
print(f'Total é de: R${total:.2f}')