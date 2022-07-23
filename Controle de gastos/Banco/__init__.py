import mysql.connector


class BancoDeDados:
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
        if self.conexao.connect():
            print('Desconexão falhou')
        else:
            print('Desconectado do banco')

    def adicionar_valor(self, valor, mes, total_compra, categoria):
        if self.conexao.connect():
            sql = 'INSERT INTO valor (registro, mes, compra_total, categoria) VALUES ({}, {}, {}, {})'\
                .format(valor, mes, total_compra, categoria)
            cursor = self.conexao.cursor()
            cursor.execute(sql)
            self.conexao.commit()
            print('Valor inserido com sucesso!')
        else:
            print('Sem conexão com o servidor')
