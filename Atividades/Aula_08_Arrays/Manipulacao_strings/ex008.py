string = input('Digite algo: ')
tamanho = len(string)
for i in range(tamanho):
    if string[i] != '.':
        print(string[i], string.count(string[i]), 'x')
        string = string.replace(string[i], '.')