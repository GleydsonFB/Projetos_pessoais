import mysql.connector


class Conector:
    def __init__(self, host, user, pword, bd):
        self.host = host
        self.user = user
        self.pasw = pword
        self.bd = bd
        self.conexao = mysql.connector.connect(host=self.host, database=self.bd, user=self.user, password=self.pasw)

    def conectar(self):
        return self.conexao

    def desconectar(self):
        self.conexao.close()
        if self.conexao.is_connected():
            print('Desconexão falhou')
        else:
            print('Desconectado do banco')

    def adicionar_valor(self, valor, mes, total_compra, categoria):
        if self.conexao.is_connected():
            sql = 'INSERT INTO valor (registro, mes, compra_total, categoria) VALUES ({}, {}, {}, {})' \
                .format(valor, mes, total_compra, categoria)
            cursor = self.conexao.cursor()
            cursor.execute(sql)
            self.conexao.commit()
            print('Valor inserido com sucesso!')
        else:
            print('Sem conexão com o servidor')

    def adicionar_compra_p(self, total_compra, parcelas):
        if self.conexao.is_connected():
            sql = 'INSERT INTO total_compra (compra, t_parcela) VALUES ("{}", "{}")' \
                .format(total_compra, parcelas)
            cursor = self.conexao.cursor()
            cursor.execute(sql)
            self.conexao.commit()
            print('Valor inserido com sucesso!')
        else:
            print('Sem conexão com o servidor')

    def select_simples(self, coluna1, coluna2, tabela):
        if self.conexao.is_connected():
            sql = f"SELECT {coluna1}, {coluna2} FROM {tabela};"
            cursor = self.conexao.cursor()
            cursor.execute(sql)
            for c1, c2 in cursor:
                return c1, c2
        else:
            print('Sem conexão com o servidor')

    def select_composto(self, total_colunas, tabela, coluna1, coluna2, colunap, pesquisa, *demais_colunas):
        if self.conexao.is_connected():
            match total_colunas:
                case 1:
                    sql = f"SELECT {coluna1} FROM {tabela} WHERE {colunap} = {pesquisa}"
                    cursor = self.conexao.cursor()
                    cursor.execute(sql)
                    for c1 in cursor:
                        return c1
                case 2:
                    sql = f"SELECT {coluna1}, {coluna2} FROM {tabela} WHERE {colunap} = {pesquisa};"
                    cursor = self.conexao.cursor()
                    cursor.execute(sql)
                    for c1, c2 in cursor:
                        return c1, c2
                case 3:
                    sql = \
                        f"SELECT {coluna1}, {coluna2}, {demais_colunas[0]} FROM {tabela} WHERE {colunap} = {pesquisa};"
                    cursor = self.conexao.cursor()
                    cursor.execute(sql)
                    for c1, c2, c3 in cursor:
                        return c1, c2, c3
                case 4:
                    sql = \
                        f"SELECT {coluna1}, {coluna2}, {demais_colunas[0]}, {demais_colunas[1]} FROM {tabela} WHERE {colunap} = {pesquisa};"
                    cursor = self.conexao.cursor()
                    cursor.execute(sql)
                    for c1, c2, c3, c4 in cursor:
                        return c1, c2, c3, c4
                case 5:
                    sql = \
                        f"SELECT * FROM {tabela} WHERE {colunap} = {pesquisa};"
                    cursor = self.conexao.cursor()
                    cursor.execute(sql)
                    for c1, c2, c3, c4, c5 in cursor:
                        return c1, c2, c3, c4, c5
        else:
            print('Sem conexão com servidor')

    def somar_gasto(self, mes, categoria='nenhuma'):
        if self.conexao.is_connected():
            if categoria == 'nenhuma':
                sql = f"SELECT SUM(registro) FROM valor WHERE mes = {mes};"
                cursor = self.conexao.cursor()
                cursor.execute(sql)
                for c1 in cursor:
                    return c1


class Categoria:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_categoria(self, nome, limite, minimo=0):
        if self.conexao.is_connected():
            sql = 'INSERT INTO categoria (nome, limite_gasto, minimo_gasto) VALUES ("{}", "{}", "{}")'.format(nome, limite, minimo)
            cursor = self.conexao.cursor()
            cursor.execute(sql)
            self.conexao.commit()
            print(f"Categoria {nome} adicionada com sucesso!")
        else:
            print('Sem conexão com o servidor')