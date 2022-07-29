from Banco import Bd

bd = Bd.Conector('localhost', 'root', 'root', 'controle_de_gastos')
conexao = bd.conectar()
categorias = Bd.Categoria(conexao)
#categorias.inserir_categoria('Jogos', 500)
compra1 = Bd.Compra(conexao)
#compra1.adicionar_compra_p(900, 9)
#compra1.adicionar_valor(90, 3, 1)
# = bd.select_composto(4, 'valor', 'registro', 'compra_total', 'id_valor', 2, 'mes', 'categoria')
#a = bd.select_simples('id_valor', 'registro', 'valor')
altera = compra1.alterar_valor(60, 6)
deleta = compra1.deletar_valor(6)