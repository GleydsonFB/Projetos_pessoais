from UtilidadesCeV import personalizacao


def leiaint(n):
    """
    --> Função para analisar se é um número inteiro!
    :param n: Recebe uma entrada onde será verificado se é um número inteiro ou não.
    :return: Retorna o número inteiro (caso seja).
    """
    while True:
        try:
            v = int(input(n))
        except(ValueError, TypeError):
            personalizacao.titulos('ERRO: Digite um número tipo inteiro!')
            continue
        except KeyboardInterrupt:
            personalizacao.titulos('ERRO: Usuário preferiu não digitar um número')
            return 0
        else:
            return v


def leiafloat(n):
    """
    --> Função para verificar se é um número real!
    :param n: Recebe uma entrada onde será analisado se é um número real.
    :return: Retorna o número real (caso seja de fato).
    """
    while True:
        try:
            v = float(input(n))
        except(TypeError):
            personalizacao.titulos('ERRO: DIGITE UM NÚMERO REAL')
            continue
        except(ValueError):
            personalizacao.titulos('ERRO: DIGITE PONTO PARA SEPARAR OS NÚMEROS AO INVÉS DE VÍRGULA\n'
                                   'E USE O SEGUINTE FORMATO: EX: 530MIL e 200 = 530200 ')
            continue
        else:
            return v


def leiadatas(n):
    """
    -- Função para inserção de datas.
    :param n: Data no formato dd.mm.
    :return: Retorna o valor formatado.
    """
    l = []
    i = []
    while True:
        ns = input(n).replace('/', '.')
        try:
            data = float(ns)
        except:
            personalizacao.titulos('Data inválida, digite apenas dia/mês')
        else:
            ds = str(data).replace('.', ' ')
            for d in ds:
                l = ds.split()
            for x, s in enumerate(l):
                i.append(int(l[x]))
            return i


def calculardatas(d1, d2):
    d = m1 = m2 = m3 = m = 0
    m = d1[1] - d2[1]
    m1 = d1[1]
    m2 = d2[1]
    m3 = m1 - m2
    if m1 > m2:
        m = m1 - (m3 - 1)
    if d1[1] in (1, 3, 5, 7, 8, 10, 12):
        d = (31 - d1[0]) + d2[0]
        m *= 31
        m -= 31
    elif d1[1] in (4, 6, 9, 11):
        d = (30 - d1[0]) + d2[0]
        m *= 30
        m -= 30
    elif d1[1] == 2:
        d = (28 - d1[0]) + d2[0]
        m *= 28
        m -= 28
    if d < 0:
        d *= -1
    if m < 0:
        m *= -1
    if m3 == -1:
        datadif = d
    else:
        datadif = d + m
    return datadif

