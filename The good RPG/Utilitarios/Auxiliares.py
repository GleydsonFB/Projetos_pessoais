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
