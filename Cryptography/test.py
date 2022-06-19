from random import randint
from Trancon import cript


desvio = randint(1, 9999)
texto = str(input('Digite: '))
converso = cript.conversor(texto, desvio)
print(converso)
tradutor = cript.tradutor(converso, desvio)
print(tradutor)
transcrito = cript.tratamento(tradutor)

