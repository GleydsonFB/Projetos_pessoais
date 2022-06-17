def valida_int(valor, msg, limite=100):
    """
    :param valor: Recebe o valor que será tratado;
    :param msg: Recebe uma mensagem personalizada que será exibida quando houver erros;
    :param limite: Recebe um número que indica quantas vezes essa função poderá ocorrer com erros (padrão é 100);
    :return: A variável tratada;
    :retorno: Retorna como True caso o limite seja atingido.
    """
    contador = 0
    while True:
        try:
            v = int(input(valor))
        except:
            print(msg)
            contador += 1
        else:
            break


def valida_float(valor, msg, limite=100):
    """
        :param valor: Recebe o valor que será tratado;
        :param msg: Recebe uma mensagem personalizada que será exibida quando houver erros;
        :param limite: Recebe um número que indica quantas vezes essa função poderá ocorrer com erros (padrão é 100);
        :return: A variável tratada;
        :retorno: Retorna como True caso o limite seja atingido.
        """
    contador = 0
    retorno = False
    while True:
        if contador >= limite:
            retorno = True
            return retorno
        try:
            v = float(input(valor))
        except:
            print(msg)
            contador += 1
        else:
            break


def valida_str(valor, msg, limite=100):
    """
        :param valor: Recebe o valor que será tratado;
        :param msg: Recebe uma mensagem personalizada que será exibida quando houver erros;
        :param limite: Recebe um número que indica quantas vezes essa função poderá ocorrer com erros (padrão é 100);
        :return: A variável tratada;
        :retorno: Retorna como True caso o limite seja atingido.
        """
    contador = 0
    retorno = False
    while True:
        if contador >= limite:
            retorno = True
            return retorno
        try:
            v = str(input(valor))
        except:
            print(msg)
            contador += 1
        else:
            break
