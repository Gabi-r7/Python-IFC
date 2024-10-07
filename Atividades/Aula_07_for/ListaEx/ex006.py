somaPositivos = 0
totalNegativos = 0
for i in range(1, 21):
    n = int(input(f"Digite o {i}º número: "))
    if n >= 0:
        somaPositivos += n
    if n < 0:
        totalNegativos += 1
print(f"A soma dos números positivos é {somaPositivos} e o total de números negativos é {totalNegativos}.")