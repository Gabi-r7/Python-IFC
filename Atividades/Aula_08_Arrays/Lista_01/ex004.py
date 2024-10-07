# Altere o algoritmo anterior para que ele realize o produto da primeira lista, pelo 
# inverso da segunda lista.

n1 = []
n2 = []
mult = []
for i in range(5):
    n1.append(int(input(f'Digite o {i+1}º valor da primeira lista: ')))
    n2.append(int(input(f'Digite o {i+1}º valor da segunda lista: ')))
    
for i in range(5):
    x = 4 - i 
    print(x)
    mult.append(n1[i] * n2[x])
    x -= 1
print(mult)