Qpaes = int(input('Digite quantos pães foram vendidos: '))
Qbroas = int(input('Digite quantas broas foram vendidos: '))
total = (Qpaes * 0.50) + (Qbroas * 1.50)
poupanca = total * 0.10
print(f'O valor total do dia é R${total};')
print(f'O valor destinado a poupança deve ser de R${poupanca}')