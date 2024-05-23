for i in range(1, 11):
    n = int(input(f"Digite o {i}º número: "))
    if i == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f"O maior número é {maior} e o menor é {menor}.")