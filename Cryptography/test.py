from random import randint
from Trancon import cript

while True:
    desvio = randint(1, 9999)
    retorno_desvio = [desvio]
    texto = str(input('Digite: '))
    converso = list(cript.conversor(texto, desvio))
    print(converso, retorno_desvio)
    tradutor = cript.tradutor(converso[0], desvio)
    print(tradutor)
    cript.tratamento(tradutor, converso[1])
    continua = int(input('\nDeseja continuar: '))
    if continua == 1:
        break