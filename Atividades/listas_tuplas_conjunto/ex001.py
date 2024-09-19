# Ler 2 duas estruturas (lista, tupla ou conjunto), denominada R de 5 elementos e
# S de 10 elementos, ambos de inteiros. Gere outra estrutura X que possua os
# elementos comuns a R e a S. Considere que na mesma estrutura não haverá
# números repetidos.
R = set()
S = set()

for i in range(5):
    R.add(int(input('Digite um número para a lista R: ')))
for i in range(10):
    S.add(int(input('Digite um número para a lista S: ')))
print(R | S)