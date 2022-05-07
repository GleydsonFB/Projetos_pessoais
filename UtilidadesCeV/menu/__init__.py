from UtilidadesCeV import personalizacao
from UtilidadesCeV import analisededados


def cabecalho(txt, cent=42, adicionais=2):
    """
    --> Função de cabeç alho simples.
    :param txt: Um texto que servirá de cabeçalho.
    :return: Retorna o mesmo texto já centralizado e com separações.
    """
    tam = len(txt)
    print('=' * (tam * adicionais))
    print(txt.center(cent))
    print('=' * (tam * adicionais))


def menu(titulomenu, *listagem):
    """
    --> Criação simples de menu.
    :param titulomenu: Seleciona o titulo do menu.
    :param listagem: Escolha os itens que irão o compor.
    :return: Retorna o menu formatado.
    """
    cabecalho(titulomenu)
    tam = len(titulomenu)
    for v, i in enumerate(listagem):
        personalizacao.titulos(f'{i.center(40)}')
    print('=' * (tam * 2))



