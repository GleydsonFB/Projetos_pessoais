from Utilitarios import Combate, Drop, Inventario, Personagens, UX
from Dados import Conexao, Crud

con = Conexao.Conector('localhost', 'root', 'root', 'tgr')
ligar_con = con.conexao_iniciada()
editor = Crud.Editor(ligar_con)
item = editor.select_where(2, 'nome', 'id', 1, 'item', 'dano')
inv = Inventario.Inventario(6, 0)
inv.adicionar(item[0]+' - Dano: '+str(item[1]))
#inv.mostrar()
arma_equipada = inv.equipar_arma()
print(arma_equipada)
