from Utilitarios import Combate, Drop, Inventario, Personagens, UX
from Dados import Conexao, Crud

con = Conexao.Conector('localhost', 'root', 'root', 'tgr')
ligar_con = con.conexao_iniciada()
editor = Crud.Editor(ligar_con)
item = editor.select_where(2, 'nome', 'id', 1, 'item', 'dano')
inv = Inventario.Inventario(6, 0)
protagonista = Personagens.Ator('Gleydson', 50, 3, 5, 8, 10)
vilao1 = Personagens.Vilao('Junior', 10, 1, 1, 1, 1, item[0], item[1])
inv.adicionar(item[0]+' - Dano: '+str(item[1]))
luta1 = Combate.Batalha(protagonista, vilao1)
batalha1 = luta1.luta(inv)
espolio1 = Combate.final_luta(batalha1, item, inv, vilao1.nome)
inv.mostrar()
b1 = luta1.luta(inv)