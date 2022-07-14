from Utilitarios import Combate, Drop, Inventario, Personagens, UX
from Dados import Conexao, Crud

con = Conexao.Conector('localhost', 'root', 'root', 'tgr')
ligar_con = con.conexao_iniciada()
editor = Crud.Editor(ligar_con)
d_vilao = editor.select_where(2, 'nome', 'vilao_id', 1, 'item', 'dano')
d_vilao1 = editor.select_where(7, 'nome', 'id', 1, 'vilao', 'hp', 'atk', 'defe', 'defe_magica', 'valor_soco', 'valor_chute')
vilao1 = Personagens.Vilao(d_vilao1[0], d_vilao1[1], d_vilao1[2], d_vilao1[3], d_vilao1[4], d_vilao1[5], d_vilao1[6])
print(vilao1.nome, vilao1.hp, vilao1.atk, vilao1.defe, vilao1.defm, vilao1.soco, vilao1.chute)
