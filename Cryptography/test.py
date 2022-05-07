from random import randint
from Cryptography import Trancon


desvio = randint(1, 9999)
texto = str(input('Digite: '))
converso = Trancon.Conversor(texto, desvio)
print(converso)
tradutor = Trancon.tradutor(converso, desvio)
print(tradutor)


