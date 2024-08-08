# Elabore um algoritmo que leia duas listas de 5 posições, após a leitura realizar a 
# soma e imprima o resultado da soma entre as duas listas de inteiros. 

n1 = []
n2 = []
soma = []
for i in range(5):
    n1.append(int(input(f'Digite o {i+1}º valor da primeira lista: ')))
    n2.append(int(input(f'Digite o {i+1}º valor da segunda lista: ')))
    soma.append(n1[i] + n2[i])
print(soma)