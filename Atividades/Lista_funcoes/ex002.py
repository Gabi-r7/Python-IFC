import random 

def isEven(a):
    print(f'A: {a}')
    if a % 2 == 0:
        return True
    else:
        return False
print(isEven(random.randint(0, 100)))