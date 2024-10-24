# Crie uma função chamada calculadora que recebe dois números e
# uma operação (adição, subtração, multiplicação ou divisão). A função
# deve retornar o resultado da operação ou uma mensagem de erro
# caso a operação seja inválida.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
nOp = int(input('- 1 Para adição\n- 2 Para subtração\n- 3 Para multiplicação\n- 4 Divisão\nDigite o número da opção: '))


def calculadora(num1, num2, numOp):
    erro = 1
    resultado = 0
    while(erro != 0):
        if numOp == 1:
            resultado = num1 + num2
        elif numOp == 2:
            resultado = num1 - num2
        elif numOp == 3:
            resultado = num1 * num2
        elif numOp == 4:
            resultado = num1 / num2
        else:
            print('Resultado inválido!')
            erro = -1
        erro = 0
    return resultado


print(f'Resultado: {calculadora(n1, n2, nOp)}')