# 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
vetor = []
soma = 0
multiplicacao = 1

for i in range(5):
    vetor.append(int(input('Digite um número inteiro: ')))
    soma += vetor[i]
    multiplicacao *= vetor[i]
print(f'Vetor: {vetor}\nSoma: {soma}\nMultiplicação: {multiplicacao}')
