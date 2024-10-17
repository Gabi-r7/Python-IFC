num = float(input('Digite um lado de quadrado: '))
area = 0

def quadrado(num):
    area = num * num
    return area

print(f'Area: {quadrado(num)}')