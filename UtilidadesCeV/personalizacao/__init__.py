def titulos(tit, cors=0):
    cor = ['\033[m',  # 0 limpa cor
           '\033[0;30;41m',  # 01 vermelho
           '\033[0;30;42m',  # 02 verde
           '\033[0;30;43m',  # 03 amarelo
           '\033[0;30;44m',  # 04 azul
           '\033[0;30;45m',  # 05 roxo
           '\033[0;30;46m', ]  # 06 branco
    tama = len(tit)
    print(tit)
    print('~' * (tama))
