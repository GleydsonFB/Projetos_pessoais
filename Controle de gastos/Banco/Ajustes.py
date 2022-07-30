import os
from time import sleep


def limpa_tela():
    """
    :return: Gera um retorno para limpar o console.
    """
    os.system('cls')


def try_padrao(dado):
    """
    Função básica para gerir erros com o código MySQL de maneira genérica.
    :param dado: Recebe um método Crud;
    :return: Retorna uma mensagem em caso de erro.
    """
    try:
        dado
    except:
        print('Erro!\nVerifique as informações digitadas e tente novamente.')
        sleep(2.5)


def valida_int(valor, msg, retorno, limite=100):
    """
    :param valor: Recebe o valor que será tratado;
    :param msg: Recebe uma mensagem personalizada que será exibida quando houver erros;
    :param retorno: Retornará uma mensagem personalizada quando o limite for superado;
    :param limite: Recebe um número que indica quantas vezes essa função poderá ocorrer com erros (padrão é 100);
    :return: A variável tratada ou 0 caso o limite seja atingido.
    """
    contador = 0
    while True:
        if contador >= limite:
            print(retorno)
            sleep(2)
            limpa_tela()
            return 0
        try:
            v = int(input(valor))
        except:
            print(msg)
            contador += 1
        else:
            return v


def valida_float(valor, msg, limite=100):
    """
        :param valor: Recebe o valor que será tratado;
        :param msg: Recebe uma mensagem personalizada que será exibida quando houver erros;
        :param limite: Recebe um número que indica quantas vezes essa função poderá ocorrer com erros (padrão é 100);
        :return: A variável tratada ou 0 caso o limite seja atingido.
        """
    contador = 0
    while True:
        if contador >= limite:
            return 0
        try:
            v = float(input(valor))
        except:
            print(msg)
            contador += 1
        else:
            return v


def valida_str(valor, msg, limite=100):
    """
        :param valor: Recebe o valor que será tratado;
        :param msg: Recebe uma mensagem personalizada que será exibida quando houver erros;
        :param limite: Recebe um número que indica quantas vezes essa função poderá ocorrer com erros (padrão é 100);
        :return: A variável tratada ou "0" caso o limite seja atingido.
        """
    contador = 0
    while True:
        if contador >= limite:
            return '0'
        try:
            v = str(input(valor))
        except:
            print(msg)
            contador += 1
        else:
            return v


def apresenta_mes():
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
             'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    for mes in range(len(meses)):
        tempo = meses[mes]
        tempo = str(tempo)
        tempo.replace('[', '')
        tempo.replace(']', '')
        tempo.replace(',', '')
        tempo.replace("'", "")
        print(f'{mes + 1} --- {tempo}')