#         Métodos necessários: 
# Create: Criar (cadastrar) 
# Read: Ler (Mostrar os dados na tela) 
# Update: Atualizar (atualizar, alterar o que o usuário deseja) 
# Delete: Apagar (Deletar o cadastro)
import time
funcionarios = []
id = 0

# Códigos de cores ANSI
RESET = "\033[m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

# Cores de texto
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

class Funcionario: 
    id = 0
    nome = ''
    cargo = ''
    salario = 0
    cpf = ''
    data_contratacao = ''

    def __init__(self, id, nome, cargo, salario, cpf, data_contratacao): 
        self.id = id # Id do funcionário
        self.nome = nome  # Nome do funcionário 
        self.cargo = cargo  # Cargo ou função desempenhada 
        self.salario = salario  # Salário do funcionário 
        self.cpf = cpf  # CPF do funcionário (identificação) 
        self.data_contratacao = data_contratacao  # Data de contratação

    def create():
        global id
        nome = input('Digite o nome do novo funcionário: ')
        cargo = input('Digite o cargo deste funcionário: ')
        salario = float(input('Digite o salário do funcionário: '))
        cpf = input('Digite o CPF do funcionário no formato "123.456.789-01": ')
        data_contratacao = input('Digite a data de contratação do funcionário no formato "DD/MM/AAAA": ')
        funcionarios.append(Funcionario(id, nome, cargo, salario, cpf, data_contratacao))
        id += 1
        print(f'\n{GREEN}{BOLD}Funcionário cadastrado!{RESET}\n')
        time.sleep(1.5)
        
    def read():
        for i in range(0, len(funcionarios)):
            print('--------------------------------------------')
            print(f'Funcionário {i+1}: ')
            print(f'Id: {funcionarios[i].id}')
            print(f'Nome: {funcionarios[i].nome}')
            print(f'Cargo: {funcionarios[i].cargo}')
            print(f'Salário: {funcionarios[i].salario:.2f}')
            print(f'CPF: {funcionarios[i].cpf}')
            print(f'Data contratação: {funcionarios[i].data_contratacao}')
        print('--------------------------------------------')
        time.sleep(3)

    def update():
        Funcionario.read()
        idEscolhido = int(input('Digite o id do funcionário a ter seus dados alterados: '))
        for i in range(0, len(funcionarios)):
            if idEscolhido == funcionarios[i].id:
                alterando = True
                while alterando:
                    atributoAlterado = int(input('0 - Voltar\n1 - Alterar o nome\n2 - Alterar o cargo\n3 - Alterar o salário\n4 - Alterar o CPF\n5 - Alterar a data de contratação\nDigite sua escolha: '))
                    match atributoAlterado:
                        case 0:
                            print(f'{BLUE}{BOLD}Voltando...{RESET}')
                            alterando = False
                            time.sleep(1.5)
                        case 1:
                            novoNome = input('Digite o novo nome do funcionário: ')
                            funcionarios[idEscolhido].nome = novoNome
                        case 2:
                            novoCargo = input('Digite o novo cargo do funcionário: ')
                            funcionarios[idEscolhido].cargo = novoCargo
                        case 3:
                            novoSalario = float(input('Digite o novo salário do funcionário: '))
                            funcionarios[idEscolhido].salario = novoSalario
                        case 4:
                            novoCpf = input('Digite o novo CPF do funcionário: ')
                            funcionarios[idEscolhido].cpf = novoCpf
                        case 5:
                            novoData = input('Digite a nova data de contratação: ')
                            funcionarios[idEscolhido].data_contratacao = novoData
                        case _:
                            print(f'\n{RED}{BOLD}Opção inválida! Tente novamente.\n{RESET}')
                            time.sleep(1.5)
            else:
                print(f'\n{RED}{BOLD}ID inválido!{RESET}\n')
                time.sleep(1.5)
    def delete():
        global funcionarios
        global id
        Funcionario.read()
        idEscolhido = int(input('Digite o id do funcionário que deseja deletar (-1 para cancelar): '))
        if idEscolhido != -1:
            for i in range(0, id):
                if idEscolhido == funcionarios[i].id:
                    del funcionarios[i]
                    print(f'{GREEN}{BOLD}Funcionário deletado!{RESET}')
                    break
                else:
                    print(f'{RED}{BOLD}Id inválido!{RESET}')
                    time.sleep(1.5)
                    break
        else:
            print(f'{BLUE}{BOLD}Cancelando...{RESET}')
            time.sleep(1.5)
                
executando = True

def menu():
    global executando
    print(f'{YELLOW}{BOLD}--------------------------------------------{RESET}')
    print(f'{CYAN}{UNDERLINE}Bem vindo ao sistema de funcionários!{RESET}')
    print(f'{YELLOW}{BOLD}--------------------------------------------{RESET}')
    while executando:
        option = int(input('0 - Parar o Programa\n1 - Cadastrar um funcionário\n2 - Ver os funcionários cadastrados\n3 - Editar um funcionário\n4 - Deletar um funcionário\nDigite sua escolha: '))
        match option:
            case 0:
                print(f'{GREEN}{BOLD}Encerrando o programa...{RESET}')
                executando = False
            case 1:
                Funcionario.create()
            case 2:
                if len(funcionarios) > 0:
                    Funcionario.read()
                else:
                    print(f'{RED}{BOLD}\nNão há funcionários cadastrados!\n{RESET}')
                    time.sleep(1.5) 
            case 3:
                if len(funcionarios) > 0:
                    Funcionario.update()
                else:
                    print(f'{RED}{BOLD}\nNão há funcionários cadastrados!\n{RESET}')
                    time.sleep(1.5) 
            case 4:
                if len(funcionarios) > 0:
                    Funcionario.delete()
                else:
                    print(f'{RED}{BOLD}\nNão há funcionários cadastrados!\n{RESET}')
                    time.sleep(1.5) 
            case _:
                print(f'{RED}{BOLD}\nErro! Tente novamente!\n{RESET}')
                time.sleep(1.5)          
menu()