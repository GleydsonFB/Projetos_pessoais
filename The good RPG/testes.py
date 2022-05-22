import Utilitarios
from Utilitarios import Inventario
from Utilitarios import Drop
import os


print('Teste')
item = 'Espada Sagrada'
drop = Drop.Drops(item)
recurso = drop.caiu('John Wick')
bag = Inventario.inventario(5)
bag.adicionar(recurso)
bag.mostrar()