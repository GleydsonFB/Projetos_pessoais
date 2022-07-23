from Banco import Bd

bd = Bd.Conector('localhost', 'root', 'root', 'controle_de_gastos')
conexao = bd.conectar()
