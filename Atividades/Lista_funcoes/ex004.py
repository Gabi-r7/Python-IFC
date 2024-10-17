base = float(input('Digite a base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))
area = 0

def Area(base, altura):
    area = (base * altura) / 2
    return area

print(f'A área do triângulo é: {Area(base, altura)}')