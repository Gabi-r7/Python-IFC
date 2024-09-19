# Ler uma estrutura (lista, tupla ou conjunto), R de 5 elementos, inteiros, contendo o
# resultado da LOTO. A seguir ler outra estrutura (lista, tupla ou conjunto), A de 10
# elementos inteiros contendo uma aposta. A seguir imprima quantos pontos fez o
# apostador.
R = set()
A = set()
for i in range(5):
    R.add(int(input('Digite o resultado da LOTO: ')))
for i in range(10):
    A.add(int(input('Digite a aposta: ')))
print(f'Acertou {len(R & A)} números')
