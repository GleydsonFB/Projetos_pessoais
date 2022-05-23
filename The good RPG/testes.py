import Utilitarios
from Utilitarios import Inventario
from Utilitarios import Drop
from Utilitarios import Personagens
import os


print('Teste')
jogador = Personagens.ator('João', 35, 11, 10, 9)
jogador.mostrar_status()
drop = Drop.Drops('Espada')
drop.caiu(jogador.nome)
bag = Inventario.inventario(5)
bag.adicionar(drop.nome_item)
bag.mostrar()
bag.remover()
bag.mostrar()