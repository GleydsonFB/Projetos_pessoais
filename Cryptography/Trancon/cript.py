def is_float(num):
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


def Dicionario(letra, desvio=0):
    Alfab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
    Element = [1.2, 1.4, 1.6, 2.1, 2.2, 2.9, 3.0, 11, 25, 9, 31, 5.5, 12, 33, 40, 4.0,
               9.9, 36, 64, 333, 44, 54, 67, 6.7, 79.1, 89.5]
    l = str(letra).lower()
    for letra, alfabeto in enumerate(Alfab):
        if l in alfabeto:
            elemento_final = Element[letra]
            return elemento_final + desvio
    if l.isnumeric() or is_float(l):
        if l.isnumeric():
            return int(l) + desvio
        else:
            return float(l) + desvio
    return l


def Conversor(msg, desvio=0):
    mensagem = list(msg)
    conversao = []
    for dado in range(len(mensagem)):
        temp = Dicionario(mensagem[dado], desvio)
        conversao.append(temp)
    return conversao


def tradutor(conv, desvio=0):
    Alfab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
    Element = [1.2, 1.4, 1.6, 2.1, 2.2, 2.9, 3.0, 11, 25, 9, 31, 5.5, 12, 33, 40, 4.0,
               9.9, 36, 64, 333, 44, 54, 67, 6.7, 79.1, 89.5]
    traducao = []
    total = 0
    for numero in range(len(conv)):
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
        for item in range(len(Element)):
            if traducao[letra] == Element[item]:
                traducao[letra] = Alfab[item]
    return str(traducao).replace("'", "")