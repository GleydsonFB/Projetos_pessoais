#Arquivo criado para espelhar package de mesmo nome;

def valida_int(valor, msg, limite=100):
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


def remove_inv(posicao, msg, espaco_total, limite=100):
    """
    :param posicao: Recebe a posicão do item que será removido;
    :param msg: Recebe uma mensagem personalizada que será exibida quando houver erros;
    :param limite: Recebe um número que indica quantas vezes essa função poderá ocorrer com erros (padrão é 100);
    :param espaco_total: Recebe o tamanho do inventário;
    :return: A variável tratada ou 0 caso o limite seja atingido.
    """
    contador = 0
    while True:
        if contador >= limite:
            return 0
        try:
            v = int(input(posicao))
        except:
            print(msg)
            contador += 1
        else:
            if v > espaco_total:
                print('Seu inventário não tem este tamanho.')
                contador += 1
            elif v <= 0:
                print(msg)
                contador += 1
            else:
                return v
