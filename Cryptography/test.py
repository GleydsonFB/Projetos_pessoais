from random import randint
from Trancon import cript


desvio = randint(1, 9999)
texto = str(input('Digite: '))
converso = cript.Conversor(texto, desvio)
print(converso)
tradutor = cript.tradutor(converso, desvio)
print(tradutor)


