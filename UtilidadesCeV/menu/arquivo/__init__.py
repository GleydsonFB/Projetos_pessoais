from UtilidadesCeV.menu import *
from UtilidadesCeV import personalizacao
from time import sleep
def arqExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(arq, mostrar=False):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo base!')
    else:
        if mostrar:
            print(f'Arquivo {arq} criado com sucesso!')


def lerarquivo(arq, menu=''):
    try:
        a = open(arq, 'rt')
    except:
        print('ERRO AO LER ARQUIVO!')
    else:
        cabecalho(menu, cent=50,adicionais=5)
        print(f'{"Título"}', f'{"Autor(a)":>20}', f'{"N° de Pág":>10}', f'{"Fim(dias)":>10}')
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]}{dado[1]:>20}{dado[2]:>10}{dado[3]:>10}')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, v1='', v2='', v3='', v4=''):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO AO ABRIR O ARQUIVO!')
    else:
        try:
            a.write(f'{v1};{v2};{v3};{v4}\n')
        except:
            print(f'Houve um erro no momento de cadastro!')
        else:
            personalizacao.titulos(f'Livro {v1} cadastrado com sucesso!', cors=5)
        finally:
            a.close()


def additem(arq, local, conteudo):
    """
    --> Função para adicionar itens a um arquivo já existente.
    :param arq: Variável do arquivo.
    :param local: Parte que será editada.
    :param conteudo: Conteúdo a ser inserido.
    :return: Retorna o conteúdo adicionado.
    """
    with open(arq, 'r') as g:
        novalinha = []
        for word in g.readlines():
            novalinha.append(word.replace(local, conteudo))
    with open(arq, 'w') as g:
        for line in novalinha:
            g.writelines(line)
    personalizacao.titulos('Alteração realizada!', cors=3)


def existeaqui(arq, nome):
    with open(arq, 'at') as a:
        a.write(nome)
        print(f'Seu perfil foi criado {nome}!')


def cadastrarcategorias(arq, totalcategorias):
    lista = []
    for v in range(totalcategorias):
        item = input(f'Qual o nome da {v + 1}° categoria: ')
        lista.append(item)
    with open(arq, 'r+') as file:
        for v, d in enumerate(lista):
            file.write(lista[v])
    print('Cadastro de categorias realizado com sucesso!')


def lercategorias(arq):
    with open(arq, 'r') as a:
        for row in a:
            category = row.split(';')
            print(f'{category}')

def somartempos(arq, valor):
    with open(arq, 'r+') as file:
        presente = float(file.read())

