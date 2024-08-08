x = 7
n = 0
while True:
    n = int(input("Tente acertar o número: "))
    if n == x:
        print('Voce acertou')
        break
    elif n > x:
        print('O numero e menor')
    elif n < x:
        print('O numero e maior')