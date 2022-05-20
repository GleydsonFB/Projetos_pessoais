from Utilitarios import Inventario
print('Teste')
item = 'Espada Sagrada'
bag = Inventario.inventario(1)
bag.mostrar()
bag.adicionar(item)
bag.mostrar()
bag.adicionar('Espada divina')
bag.mostrar()