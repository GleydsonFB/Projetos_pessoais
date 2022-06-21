from random import randint
from Trancon import cript

while True:
    desvio = randint(1, 9999)
    texto = str(input('Digite: '))
    converso = cript.conversor(texto, desvio)
    print(converso)
    tradutor = cript.tradutor(converso[0], desvio)
    print(tradutor)
    cript.tratamento(tradutor, converso[1])
    continua = int(input('\nDeseja continuar: '))
    if continua == 1:
        break