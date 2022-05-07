from UtilidadesCeV import analisededados
from UtilidadesCeV import menu
from UtilidadesCeV.menu import arquivo
from time import sleep
from UtilidadesCeV import personalizacao
import os
from UtilidadesCeV import funcoes_SSA
xps = 'valorxp.txt'
if arquivo.arqExiste(xps) is False:
    arquivo.criararquivo(xps)
personalizacao.titulos('Bem vindo(a) à calculadora de XP SSA By Gleydson')
sleep(2)
while True:
    menu.menu('Selecione uma opção', '1 - Cadastrar perfil', '2 - Calcular XP diária', '3 - Tempo médio de santo do 1 ao 80', '4 - Redefinir valores', '5 - Sair do programa')
    escolha = analisededados.leiaint(': ')
    if os.stat(xps).st_size == 0:
        personalizacao.titulos('Você ainda não cadastrou o perfil, por favor, faça isso')
        sleep(3)
        personalizacao.titulos(
            'Para calcular os valores com precisão, faça uma luta de Ruínas e um Cérbero solo e sem reforço!')
        l = funcoes_SSA.xpmedia('Quanto ganhou de xp total na luta contra o Cérbero SEM REFORÇO: ',
                                'Quanto ganhou de xp total na luta normal de Ruínas SEM REFORÇO: ',
                                'Qual andar você está atualmente: ')
        funcoes_SSA.cadastrarxp(xps, l[0], l[1], l[2])
        print('Perfil cadastrado!')
        sleep(3)
    elif escolha == 1:
        personalizacao.titulos('Para calcular os valores com precisão, faça uma luta de ruinas e um cerberus solo e sem reforço!')
        l = funcoes_SSA.xpmedia('Quanto ganhou de xp total na luta contra o Cérbero SEM REFORÇO: ', 'Quanto ganhou de xp total na luta normal de Ruínas SEM REFORÇO: ', 'Qual andar você está atualmente: ')
        funcoes_SSA.cadastrarxp(xps, l[0], l[1], l[2])
        sleep(3)
    elif escolha == 2 and os.stat(xps).st_size == 0:
        personalizacao.titulos('Você ainda não cadastrou o perfil, por favor, faça isso')
        sleep(3)
        personalizacao.titulos(
            'Para calcular os valores com precisão, faça uma luta de Ruínas e um Cérbero solo e sem reforço!')
        l = funcoes_SSA.xpmedia('Quanto ganhou de xp total na luta contra o Cérbero SEM REFORÇO: ',
                                'Quanto ganhou de xp total na luta normal de Ruínas SEM REFORÇO: ',
                                'Qual andar você está atualmente: ')
        funcoes_SSA.cadastrarxp(xps, l[0], l[1], l[2])
        print('Perfil cadastrado!')
        sleep(3)
    elif escolha == 2:
        xp = funcoes_SSA.calculoxp(xps,'Quanto de vigor irá farmar hoje: ')
    elif escolha == 3:
        xp = funcoes_SSA.santo80(xps)
    elif escolha == 4:
        a = str(input('Tem certeza que deseja redefinir o perfil de XPs? [S/N] ')).strip()
        while a not in 'SsNn':
            a = str(input('Digite S ou N: ')).strip()
        if a in 'Ss':
            os.remove(xps)
            print('Dados reiniciados com sucesso.')
            sleep(2)
    elif escolha == 5:
        personalizacao.titulos('Fechando o programa, volte sempre!')
        sleep(3)
        break
    else:
        personalizacao.titulos('Opção Inválida')
        sleep(1)