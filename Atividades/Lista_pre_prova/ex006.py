aluninhos = {'Fake': 7, 'Pedro': 2, 'Gabriel': 10}
print(f'Alunos no sistema: {aluninhos.keys()}')
aux = input('Digite o nome de um dos alunos: ')
if aux in aluninhos:
    print(f'Nota de {aux}: {aluninhos[aux]}')
else:
    print('Aluninho não encontrado!')