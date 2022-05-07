def aumentar(a, b, cnt=False):
    v = a + (a * (b/100))
    if cnt:
        return contabil(v)
    else:
        return v


def diminuir(a, b, cnt=False):
    v = a - (a * (b/100))
    if cnt:
        return contabil(v)
    else:
        return v


def dobro(a, cnt=False):
    v = a * 2
    if cnt:
        return contabil(v)
    else:
        return v


def triplo(a, cnt=False):
    v = a * 3
    if cnt:
        return contabil(v)
    else:
        return v


def metade(a, cnt=False):
    v = a / 2
    if cnt:
        return contabil(v)
    else:
        return v


def contabil(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(valor, aumento=5, reducao=10):
    v = valor
    print('-' * 30)
    print(f'RESUMO DE PREÇOS'.center(30))
    print('-' * 30)
    print(f'Preço analisado \t{contabil(v)}')
    print(f'Dobro do preço \t\t{dobro(v, True)}')
    print(f'Aumento de {aumento}%: \t{aumentar(v, aumento, True)}')
    print(f'Redução de {reducao}%: \t{diminuir(v, reducao, True)}')
    print('-' * 30)



