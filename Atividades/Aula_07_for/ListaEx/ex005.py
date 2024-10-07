total = 0
for i in range(1, 16):
    n = int(input(f"Digite o {i}º número: "))
    if n > 30:
        total += 1
print(f"O total de números maiores que 30 é {total}.")