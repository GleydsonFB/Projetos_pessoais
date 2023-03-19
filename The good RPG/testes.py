from Utilitarios import Combate, Drop, Inventario, Personagens, UX
from Dados import Conexao, Crud

con = Conexao.Conector('localhost', 'root', 'root', 'tgr')
ligar_con = con.conexao_iniciada()
editor = Crud.Editor(ligar_con)
vilao = editor.select_where(6, 'nome', 'id', 1, 'vilao', 'hp', 'atk', 'defe', 'valor_soco', 'valor_chute')
item = editor.select_where(2, 'nome', 'id', 1, 'item', 'dano')
inv = Inventario.Inventario(6, 0)
protagonista = Personagens.Ator('Gleydson', 50, 3, 5, 8, 10)
print(vilao[0])
vilao1 = Personagens.Vilao(vilao[0], vilao[1], vilao[2], vilao[3],
                           vilao[4], vilao[5], item[0], item[1])
inv.adicionar(item[0]+' - Dano: '+str(item[1]))
luta1 = Combate.Batalha(protagonista, vilao1)
batalha1 = luta1.luta(inv)
espolio1 = Combate.final_luta(batalha1, item, inv, vilao1.nome)
inv.mostrar()
b1 = luta1.luta(inv)