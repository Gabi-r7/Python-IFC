# Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x e 
# mostre os 10 valores armazenados. 

x = []
for i in range(10):
    x.append(int(input(f'Digite o {i+1}º valor: ')))
print(x)