# 19. Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações: 
# "Qual o melhor Sistema Operacional para uso em servidores?" 
# As possíveis respostas são: 
# 1- Windows Server 
# 2- Unix 
# 3- Linux 
# 4- Netware 
# 5- Mac OS 
# 6- Outro 
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte: 
# Sistema Operacional Votos % 
# ------------------- ----- --- 
# Windows Server 1500 17% 
# Unix 3500 40%
# Linux 3000 34% 
# Netware 500 5% 
# Mac OS 150 2% 
# Outro 150 2% 
# ------------------- ----- 
# Total 8800 
# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos. 
options = []
votos_windows_server = 0
votos_unix = 0
votos_linux = 0
votos_netware = 0
votos_mac_os = 0
votos_outro = 0
total_votos = 0

while True:
    last_vote = (int(input('Digite um número para votar na enquete: As possíveis respostas são:\n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\nSua escolha: ')))
    
    if last_vote == 0:
        break
    elif last_vote == 1:
        votos_windows_server += 1
    elif last_vote == 2:
        votos_unix += 1
    elif last_vote == 3:
        votos_linux += 1
    elif last_vote == 4:
        votos_netware += 1
    elif last_vote == 5:
        votos_mac_os += 1
    elif last_vote == 6:
        votos_outro += 1
    else:
        print('Voto inválido!')
    
    options.append(last_vote)

total_votos = len(options)

if total_votos > 0:
    perc_windows_server = (votos_windows_server / total_votos) * 100
    perc_unix = (votos_unix / total_votos) * 100
    perc_linux = (votos_linux / total_votos) * 100
    perc_netware = (votos_netware / total_votos) * 100
    perc_mac_os = (votos_mac_os / total_votos) * 100
    perc_outro = (votos_outro / total_votos) * 100

    print(f'Sistema Operacional     Votos   %')
    print(f'-------------------     -----   ---')
    print(f'Windows Server          {votos_windows_server}     {perc_windows_server:.2f}%')
    print(f'Unix                    {votos_unix}     {perc_unix:.2f}%')
    print(f'Linux                   {votos_linux}     {perc_linux:.2f}%')
    print(f'Netware                 {votos_netware}     {perc_netware:.2f}%')
    print(f'Mac OS                  {votos_mac_os}     {perc_mac_os:.2f}%')
    print(f'Outro                   {votos_outro}     {perc_outro:.2f}%')
    print(f'-------------------     -----')
    print(f'Total                   {total_votos}')

    max_votos = max(votos_windows_server, votos_unix, votos_linux, votos_netware, votos_mac_os, votos_outro)
    if max_votos == votos_windows_server:
        vencedor = "Windows Server"
    elif max_votos == votos_unix:
        vencedor = "Unix"
    elif max_votos == votos_linux:
        vencedor = "Linux"
    elif max_votos == votos_netware:
        vencedor = "Netware"
    elif max_votos == votos_mac_os:
        vencedor = "Mac OS"
    else:
        vencedor = "Outro"

    print(f'O Sistema Operacional mais votado foi o {vencedor}, com {max_votos} votos, correspondendo a {max_votos / total_votos * 100:.2f}% dos votos.')
else:
    print('Nenhum voto foi registrado.')