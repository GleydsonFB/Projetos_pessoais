from Banco import Bd

bd = Bd.Conector('localhost', 'root', 'root', 'controle_de_gastos')
Compras = Bd.Compra(bd.conectar())
anti = Bd.Compra.antecipar_compra_p(Compras, 48, 1, 2023, 5)