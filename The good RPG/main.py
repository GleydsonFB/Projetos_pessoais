import Utilitarios
from Utilitarios import Inventario
import os


print('Teste')
item = 'Espada Sagrada'
bag = Inventario.inventario(5)
bag.adicionar(item)
bag.remover()
bag.mostrar()