import random

def maior(a, b):
    print(f'A: {a}')
    print(f'B: {b}')
    if a > b:
        return a
    else: 
        return b

print(f'Maior: {maior (random.randint(0, 100), random.randint(0, 100))}')