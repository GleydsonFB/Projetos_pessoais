import Utilitarios
from Utilitarios import Inventario
from Utilitarios import Drop
from Utilitarios import Personagens


print('Teste')
drop = Drop.Drops('Espada')
bag = Inventario.inventario(5, 0)
bag.adicionar(drop.caiu('Noob'), drop.grana())
npc_joao = Personagens.npc('João', ['Espada', 'Lança', 'Escudo'], [2, 4, 8])
bag.mostrar()
npc_joao.compras('eu', bag)
bag.mostrar()
