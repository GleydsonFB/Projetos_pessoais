from UtilidadesCeV import analisededados
from UtilidadesCeV import personalizacao
from time import sleep


def xpmedia(cerberus, golem, andar, xpmigo=0):
    c = analisededados.leiafloat(cerberus)
    g = analisededados.leiafloat(golem)
    a = analisededados.leiaint(andar)
    while a not in range(1, 12):
        a = analisededados.leiaint('Digite um andar válido (entre 1 e 11): ')
    f = str(input('Irá fazer com um amigo/Conta farm? [S/N] ')).strip()
    while f not in 'SsNn':
        f = str(input('Digite S ou N: ')).strip()
    if f in 'Ss':
        x = analisededados.leiaint('Qual o bônus de amizade? de 1 a 5%: ')
        while x not in range(1, 6):
            x = analisededados.leiaint('Digite um bônus válido: ')
    else:
        x = xpmigo
    b = str(input('Está com reforço ativo? [S/N] ')).strip()
    while b not in 'SsNn':
        b = str(input('Digite [S ou N]: ')).strip()
    if x != 0:
        x = x / 100
    else:
        x = 1
    fm = str(input('Será automático (a) ou manual (m) o farm? '))
    while fm not in 'AaMm':
        fm = str(input('Digite A para automático ou M para manual: '))
    if fm in 'Aa' and b in 'Ss':
        xrc = ((c * 0.20) + c)
        xrc1 = (xrc * x) + xrc
        xrg = ((g * 0.20) + g)
        xrg1 = (xrg * x) + xrg
        return xrc1, xrg1, a
    elif fm in 'Aa':
        xc = (c * x) + c
        xg = (g * x) + g
        return xc, xg, a
    else:
        if b in 'Ss':
            xrc = ((c * 0.20) + c)
            xrc1 = (xrc * x) + xrc
            xpe = (xrc1 * 0.20) + xrc1
            xrg = ((g * 0.20) + g)
            xrg1 = (xrg * x) + xrg
            xpeg = (xrg1 * 0.20) + xrg1
            return xpe, xpeg, a
        else:
            xc = (c * x) + c
            xpec = (xc * 0.20) + xc
            xg = (g * x) + g
            xpeg = (xg * 0.20) + xc
            return xpec, xpeg, a


def cadastrarxp(arq, c, g, a):
    with open(arq, 'r+') as file:
        file.write(f'{c};{g};{a}')


def calculoxp(arq, vigor):
    lista = []
    with open(arq, 'r+') as file:
        linha = file.read().split(';')
        for linhas in linha:
            lista.append(float(linhas))
    v = analisededados.leiaint(vigor)
    e = str(input('Vai farmar apenas Cérbero ou apenas Golem? [S/N] ')).strip()
    while e not in 'SsNn':
        e = str(input('Digite S ou N, se for farmar apenas Ruínas ou apenas Cérbero hoje: ')).strip()
    if e in 'Ss':
        ef = analisededados.leiaint('Será Cérbero[1] ou Ruínas normal[2]: ')
        while ef not in range(1, 3):
            ef = analisededados.leiaint('Escolha 1 para Cérbero ou 2 para Ruínas: ')
        if ef == 1:
            fc = v / 30
            if fc == float(fc):
                fc = int(fc - 1)
            vfc = lista[0] * fc
            personalizacao.titulos(f'Com o XP que você ganha em cada Cérbero ({lista[0]:,}), você irá farmar {fc} vezes e obterá {vfc:,.0f} de xp (arredondado)')
            sleep(4)
        else:
            fg = v / 6
            if fg == float(fg):
                fg = int(fg - 1)
            vfg = lista[1] * fg
            personalizacao.titulos(f'Com o XP que você ganha em cada Ruína ({lista[1]:,}), você irá farmar {fg} vezes e obterá {vfg:,.0f} de xp (arredondado)')
            sleep(4)
    else:
        print('Nesse caso precisa definir quantos % do XP irá para cada tipo de farm:')
        while True:
            tipoc = analisededados.leiafloat('Quantos % irá para Cérbero: ')
            tipog = analisededados.leiafloat('Quantos % irá para Ruínas: ')
            if (tipoc + tipog) < 100 or (tipoc + tipog) > 100:
                print('Porcentagens inválidas, a soma das duas deve ser igual a 100%')
            else:
                break
        xp_porcentoc = v * (tipoc / 100)
        xp_porcentog = v - xp_porcentoc
        fc = xp_porcentoc / 30
        fg = xp_porcentog / 6
        if fc == float(fc):
            fc = int(fc - 1)
        if fg == float(fg):
            fg = int(fg - 1)
        xpc = lista[0] * fc
        xpg = lista[1] * fg
        personalizacao.titulos(f'Com {tipoc}% do seu vigor gastos em Cérbero, você farmará {fc} vezes e obterá {xpc:,} de XP')
        personalizacao.titulos(f'Com {tipog}% do seu vigor gastos em Ruínas, você farmará {fg} vezes e obterá {xpg:,} de XP')
        sleep(5)


def santo80(arq):
    lista = []
    xp_necessaria = 62000000
    with open(arq, 'r+') as file:
        linha = file.read().split(';')
        for linhas in linha:
            lista.append(float(linhas))
    vigor = analisededados.leiaint('Quanto de vigor pretende farmar por dia: ')
    e = str(input('Vai farmar apenas Cérbero ou apenas Ruínas? [S/N] ')).strip()
    while e not in 'SsNn':
        e = str(input('Digite S ou N, se for farmar apenas ruinas ou apenas cerberus hoje: ')).strip()
    if e in 'Ss':
        ef = analisededados.leiaint('Será Cérbero[1] ou Ruínas normal[2]: ')
        while ef not in range(1, 3):
            ef = analisededados.leiaint('Escolha 1 para Cérbero ou 2 para Ruínas: ')
        if ef == 1:
            fc = vigor / 30
            if fc == float(fc):
                fc = int(fc - 1)
            xp_dia = lista[0] * fc
            xp_total = xp_necessaria / xp_dia
            personalizacao.titulos(f'Com os dados informados para Cérbero, você levaria {xp_total:.0f} dias aproximadamente '
                                   f'para ter um cavaleiro do 1 ao 80, considerando que você teria 0 de xp ao iniciar.')
            sleep(4)
        elif ef == 2:
            fg = vigor / 6
            if fg == float(fg):
                fg = int(fg - 1)
            xp_dia = lista[1] * fg
            xp_total = xp_necessaria / xp_dia
            personalizacao.titulos(f'Com os dados informados para Ruínas normal, você levaria {xp_total:.0f} dias aproximadamente'
                                   f' para ter um cavaleiro do 1 ao 80, considerando que você teria 0 de xp ao iniciar')
            sleep(4)
    else:
        print('Nesse caso precisa definir quantos % do XP irá para cada tipo de farm:')
        while True:
            tipoc = analisededados.leiafloat('Quantos % irá para Cérbero: ')
            tipog = analisededados.leiafloat('Quantos % irá para Ruínas: ')
            if (tipoc + tipog) < 100 or (tipoc + tipog) > 100:
                print('Porcentagens inválidas, a soma das duas deve ser igual a 100%')
            else:
                break
        xp_porcentoc = vigor * (tipoc / 100)
        xp_porcentog = vigor - xp_porcentoc
        fc = xp_porcentoc / 30
        fg = xp_porcentog / 6
        if fc == float(fc):
            fc = int(fc - 1)
        if fg == float(fg):
            fg = int(fg - 1)
        xpc = lista[0] * fc
        xpg = lista[1] * fg
        xp_total = xpc + xpg
        xp_total80 = xp_necessaria / xp_total
        personalizacao.titulos(f'Gastando todos os dias {vigor} de vigor para com as porcentagens de Cérbero/Ruína escolhida ({tipoc}% e {tipog}%) você levará {xp_total80:.0f} dias para ter um cavaleiro do 1 ao 80')
        sleep(5)