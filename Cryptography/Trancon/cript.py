def is_float(num):
    """
    Função criada para tratar erros de tipo;
    :param num: Recebe um valor para verificação;
    :return: Retorna como falso ou verdadeiro, isso serve de base para a conversão dentro da classe;
    """
    try:
        int(num)
    except ValueError:
        try:
            float(num)
        except ValueError:
            return False
        else:
            return True
    else:
        return False


def letra_mai(texto):
    """
    Função para converter letras maiusculas em simbolos;
    :param texto: Recebe o texto que será convertido;
    :return: Retorna uma lista com a conversão, indicando @ na posição de uma letra maiuscula;
    """
    maiusculas = []
    for letra in range(len(texto)):
        temporario = texto[letra]
        temporario = str(temporario)
        if temporario.isupper():
            maiusculas.append('@')
        else:
            maiusculas.append('!')
    return maiusculas


def dicionario(letra, desvio=0):
    """
    Função principal da criptografia, ela define a lista base bem como faz a conversão do texto para números;
    :param letra: Recebe a letra que será tratada;
    :param desvio: Recebe o valor de desvio, usado para dificultar a descriptografia;
    :return: Retorna a letra convertida em um número com desvio embutido;
    """
    alfab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
    element = [1.2, 1.4, 1.6, 2.1, 2.2, 2.9, 3.0, 11, 25, 9, 31, 5.5, 12, 33, 40, 4.0,
               9.9, 36, 64, 333, 44, 54, 67, 6.7, 79.1, 89.5]
    l = str(letra).lower()
    for letra, alfabeto in enumerate(alfab):
        if l in alfabeto:
            elemento_final = element[letra]
            return elemento_final + desvio
    if l.isnumeric() or is_float(l):
        if l.isnumeric():
            return int(l) + desvio
        else:
            return float(l) + desvio
    return l


def conversor(msg, desvio=0):
    """
    Função conversora do texto;
    :param msg: Recebe o texto que será convertido;
    :param desvio: Recebe o desvio, parâmetro para dificultar a descriptografia;
    :return: Retorna o texto transformado em números juntamente com a posição das letras maiúsculas;
    """
    mensagem = list(msg)
    conversao = []
    maisculas = letra_mai(list(msg))
    for dado in range(len(mensagem)):
        temp = dicionario(mensagem[dado], desvio)
        conversao.append(temp)
    conversao.append(desvio)
    return conversao, maisculas


def tradutor(conv, desvio=0):
    """
    Função que desfaz a conversão, retornando ao texto original;
    :param conv: Recebe o texto criptografado;
    :param desvio: Recebe o desvio usado na conversão;
    :return: Retorna o texto já descriptografado em forma de lista;
    """
    alfab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
    element = [1.2, 1.4, 1.6, 2.1, 2.2, 2.9, 3.0, 11, 25, 9, 31, 5.5, 12, 33, 40, 4.0,
               9.9, 36, 64, 333, 44, 54, 67, 6.7, 79.1, 89.5]
    traducao = []
    total = len(conv)
    total -= 1
    for numero in range(total):
        temp = str(conv[numero])
        if is_float(temp):
            temp = float(temp)
            temp -= desvio
            valor = round(temp, 1)
            traducao.append(valor)
        elif temp.isnumeric():
            valor = int(temp)
            valor -= desvio
            traducao.append(valor)
        else:
            traducao.append(temp)
    for letra in range(len(traducao)):
        for item in range(len(element)):
            if traducao[letra] == element[item]:
                traducao[letra] = alfab[item]
    return traducao


def tratamento(transcricao, letras_m):
    """
    Função simples para transformar a lista no texto original;
    :param transcricao: Recebe a lista da tradução;
    :param letras_m: Recebe a lista contendo a posição das letras maiúsculas;
    :return: Retorna o texto original;
    """
    for letra in range(len(transcricao)):
        resultado = transcricao[letra]
        resultado = str(resultado)
        resultado.replace("'", '')
        resultado.replace('[', '')
        resultado.replace(']', '')
        resultado.replace(',', '')
        if letras_m[letra] == '@':
            l_mai = resultado.upper()
            print(l_mai, end='')
        else:
            print(resultado, end='')