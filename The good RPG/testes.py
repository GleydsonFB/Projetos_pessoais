from Utilitarios import Combate, Drop, Inventario, Personagens, UX
from Dados import Conexao, Crud

banco = Conexao.Conector('localhost', 'root', 'root', 'tgr')
a = banco.conexao_iniciada()
edit = Crud.Editor(a)
edit.insert_inv('Um', 1)
banco.conexao_finalizada()