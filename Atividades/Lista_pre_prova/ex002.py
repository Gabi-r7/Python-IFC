tupla = ("maçã", "banana", "laranja", "abacaxi", "uva")
fruta = input('Digite uma fruta para verificar se ela esta na tupla: ')
for i in range(0, len(tupla)):
    if tupla[i] == fruta:
        tem = True
        break
    else:
        tem = False
if tem:
    print('A fruta está na tupla')
else:
    print('A fruta não está na tupla')