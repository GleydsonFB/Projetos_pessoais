from .Conexao import Conector
import mysql.connector


class Editor:
    def __init__(self, conexao_on):
        self.con = conexao_on

    def select(self, coluna1, coluna2, tabela):
        if self.con.is_connected():
            sql = f"SELECT {coluna1}, {coluna2} FROM {tabela};"
            cursor = self.con.cursor()
            cursor.execute(sql)
            for c1, c2 in cursor:
                print(c1, c2)
        else:
            print('Sem conexão com o servidor.')

    def insert_inv(self, item, gold):
        if self.con.is_connected():
            sql = f"INSERT INTO inventario (nome_slot, gold) VALUES ("
            comando = f"{item}, {gold})"
            comando_sql = sql + comando
            cursor = self.con.cursor()
            cursor.execute(comando_sql)
            self.con.commit()
        else:
            print('Sem conexão com o servidor.')