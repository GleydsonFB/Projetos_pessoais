from .Conexao import Conector


class Editor:
    def __init__(self, conexao_on):
        self.con = conexao_on

    def select(self, coluna1, coluna2, tabela):
        if self.con.is_connected():
            sql = f"SELECT {coluna1}, {coluna2} FROM {tabela};"
            cursor = self.con.cursor()
            cursor.execute(sql)
            for c1, c2 in cursor:
                return c1, c2
        else:
            print('Sem conexão com o servidor.')

    def insert_inv(self, item, gold=0):
        if self.con.is_connected():
            sql = "INSERT INTO inventario (nome_slot, gold) VALUES ('{}', '{}')".format(item, gold)
            cursor = self.con.cursor()
            cursor.execute(sql)
            self.con.commit()
            print('item inserido com sucesso.')
        else:
            print('Sem conexão com o servidor.')

    def select_where(self, total_coluna, coluna1, coluna_p, dado_proc, tabela, *colunas):
        if self.con.is_connected():
            match total_coluna:
                case 1:
                    sql = f"SELECT {coluna1} FROM {tabela} WHERE {coluna_p} = {dado_proc}"
                    cursor = self.con.cursor()
                    cursor.execute(sql)
                    for item in cursor:
                        return item
                case 2:
                    sql = f"SELECT {coluna1}, {colunas[0]} FROM {tabela} WHERE {coluna_p} = {dado_proc}"
                    cursor = self.con.cursor()
                    cursor.execute(sql)
                    for item in cursor:
                        return item
                case 3:
                    sql = f"SELECT {coluna1}, {colunas[0]}, {colunas[1]} FROM {tabela} WHERE {coluna_p} = {dado_proc}"
                    cursor = self.con.cursor()
                    cursor.execute(sql)
                    for item in cursor:
                        return item
                case 4:
                    sql = f"SELECT {coluna1}, {colunas[0]}, {colunas[1]}, {colunas[2]} FROM {tabela} WHERE {coluna_p} = {dado_proc}"
                    cursor = self.con.cursor()
                    cursor.execute(sql)
                    for item in cursor:
                        return item
                case 5:
                    sql = f"SELECT {coluna1}, {colunas[0]}, {colunas[1]}, {colunas[2]}, {colunas[3]} FROM {tabela} WHERE {coluna_p} = {dado_proc}"
                    cursor = self.con.cursor()
                    cursor.execute(sql)
                    for item in cursor:
                        return item
                case 6:
                    sql = f"SELECT {coluna1}, {colunas[0]}, {colunas[1]}, {colunas[2]}, {colunas[3]}, {colunas[4]} FROM {tabela} WHERE {coluna_p} = {dado_proc}"
                    cursor = self.con.cursor()
                    cursor.execute(sql)
                    for item in cursor:
                        return item
                case 7:
                    sql = f"SELECT {coluna1}, {colunas[0]}, {colunas[1]}, {colunas[2]}, {colunas[3]}, {colunas[4]}, {colunas[5]} FROM {tabela} WHERE {coluna_p} = {dado_proc}"
                    cursor = self.con.cursor()
                    cursor.execute(sql)
                    for item in cursor:
                        return item
                case _:
                    print('Total de colunas informada maior que o permitido.')

    def delete_value(self, tabela, busca, pesquisa):
        if self.con.is_connected:
            sql = f"DELETE FROM {tabela} WHERE {busca} = {pesquisa};"
            cursor = self.con.cursor()
            cursor.execute(sql)
            self.con.commit()
            print('Dado deletado')
        else:
            print('Sem conexão com o servidor')


