from time import sleep
import os


def texto_tela(frase, tempo=0.3):
    """
    :param frase: Recebe uma frase que será tratada;
    :param tempo: Recebe o tempo em segundos para duração;
    :return: Retorna a mesma frase só que utilizando sleeps para gerar imersão.
    """
    frase_tratada = list(frase)
    for letra in range(len(frase_tratada)):
        print(f'{frase_tratada[letra]}', end='')
        sleep(tempo)


def limpa_tela():
    """
    :return: Gera um retorno para limpar o console.
    """
    os.system('cls')


#texto_tela('Essa frase é de teste', 0.3)