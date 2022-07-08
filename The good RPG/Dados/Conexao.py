import mysql.connector


class Conector:
    def __init__(self, host, user, passw, db):
        self.host = host
        self.user = user
        self.password = passw
        self.database = db
        self.con = mysql.connector.connect()

    def conexao_iniciada(self):
        self.con = mysql.connector.connect\
            (host=self.host, database=self.database, user=self.user, password=self.password)
        return self.con

    def conexao_finalizada(self):
        self.con.close()
        if self.con.is_connected():
            print('Falhou')
        else:
            print('Conexão finalizada')




cone = Conector('localhost', 'root', 'root', 'sakila')
a = cone.conexao_iniciada()
