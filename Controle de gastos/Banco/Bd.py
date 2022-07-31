import datetime
import mysql.connector

data = datetime.datetime.now()
ano = data.date()


class Conector:
    def __init__(self, host, user, pword, bd):
        self.host = host
        self.user = user
        self.pasw = pword
        self.bd = bd
        self.conexao = mysql.connector.connect(host=self.host, database=self.bd, user=self.user, password=self.pasw)
        self.cursor = self.conexao.cursor()

    def conectar(self):
        return self.conexao

    def desconectar(self):
        self.conexao.close()

    def select_ultimo(self, nome_id, tabela):
        if self.conexao.is_connected():
            sql = f'SELECT MAX({nome_id}) FROM {tabela}'
            self.cursor.execute(sql)
            for c1 in self.cursor:
                return c1

    def select_simples(self, coluna1, coluna2, tabela):
        if self.conexao.is_connected():
            sql = f"SELECT {coluna1}, {coluna2} FROM {tabela};"
            self.cursor.execute(sql)
            for c1, c2 in self.cursor:
                return c1, c2
        else:
            print('Sem conexão com o servidor.')

    def select_composto(self, total_colunas, tabela, coluna1, colunap, pesquisa, *demais_colunas):
        if self.conexao.is_connected():
            match total_colunas:
                case 1:
                    sql = f"SELECT {coluna1} FROM {tabela} WHERE {colunap} = {pesquisa}"
                    self.cursor.execute(sql)
                    for c1 in self.cursor:
                        return c1
                case 2:
                    sql = f"SELECT {coluna1}, {demais_colunas[0]} FROM {tabela} WHERE {colunap} = {pesquisa};"
                    self.cursor.execute(sql)
                    for c1, c2 in self.cursor:
                        return c1, c2
                case 3:
                    sql = \
                        f"SELECT {coluna1}, {demais_colunas[0]}, {demais_colunas[1]} FROM {tabela} WHERE {colunap} = {pesquisa};"
                    self.cursor.execute(sql)
                    for c1, c2, c3 in self.cursor:
                        return c1, c2, c3
                case 4:
                    sql = \
                        f"SELECT {coluna1}, {demais_colunas[0]}, {demais_colunas[1]}, {demais_colunas[2]} FROM {tabela} WHERE {colunap} = {pesquisa};"
                    self.cursor.execute(sql)
                    for c1, c2, c3, c4 in self.cursor:
                        return c1, c2, c3, c4
                case 5:
                    sql = \
                        f"SELECT * FROM {tabela} WHERE {colunap} = {pesquisa};"
                    self.cursor.execute(sql)
                    for c1, c2, c3, c4, c5 in self.cursor:
                        return c1, c2, c3, c4, c5
        else:
            print('Sem conexão com servidor.')


class Categoria:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def inserir_categoria(self, nome, limite, minimo=0):
        if self.conexao.is_connected():
            if minimo != 0:
                sql = 'INSERT INTO categoria (nome, limite_gasto, minimo_gasto) VALUES ("{}", "{}", "{}")'.format(nome, limite, minimo)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f"Categoria {nome} adicionada com sucesso!")
            else:
                sql = 'INSERT INTO categoria (nome, limite_gasto) VALUES ("{}", "{}")'.format(nome, limite)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f"Categoria {nome} adicionada com sucesso!")
        else:
            print('Sem conexão com o servidor.')

    def alterar_categoria(self, id_cat, nome='', limite='', minimo=''):
        if self.conexao.is_connected():
            if nome != '' and limite == '' and minimo == '':
                sql = 'UPDATE categoria SET nome = "{}" WHERE id_cat = "{}"'.format(nome, id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Novo nome da categoria definido como {nome}!')
            elif nome != '' and limite != '' and minimo == '':
                sql = 'UPDATE categoria SET nome = "{}", limite_gasto = "{}" WHERE id_cat = "{}"'.format(nome, limite, id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Alterado nome e limite para: {nome} e {limite}!')
            elif nome != '' and limite != '' and minimo != '':
                sql = 'UPDATE categoria SET nome = "{}", limite_gasto = "{}", minimo_gasto = "{}" WHERE id_cat = "{}"'.format(nome, limite, minimo, id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Alterado nome, limite e minimo gasto para: {nome}, R${limite} e R${minimo}!')
            elif nome == '' and limite != '' and minimo == '':
                sql = 'UPDATE categoria SET limite_gasto = "{}" WHERE id_cat = "{}"'.format(limite, id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Novo limite definido para R${limite}!')
            elif nome == '' and limite != '' and minimo != '':
                sql = 'UPDATE categoria SET limite_gasto = "{}", minimo_gasto = "{}" WHERE id_cat = "{}"'.format(limite, minimo, id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Novo limite definido para R${limite} e mínimo de R${minimo}!')
            elif nome == '' and limite == '' and minimo != '':
                sql = 'UPDATE categoria SET minimo_gasto = "{}" WHERE id_cat = "{}"'.format(minimo, id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Novo valor mínimo definido para R${minimo}!')
            elif nome != '' and limite == '' and minimo != '':
                sql = 'UPDATE categoria SET nome = "{}", minimo_gasto = "{}" WHERE id_cat = "{}"'.format(nome, minimo, id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Nome alterado para {nome} e com novo valor mínimo de R${minimo}!')
            else:
                print('Opção inválida.')

    def deletar_categoria(self, id_cat, nome):
        if self.conexao.is_connected():
            sql = f'DELETE FROM categoria WHERE id_cat = {id_cat}'
            self.cursor.execute(sql)
            self.conexao.commit()
            print(f'Categoria {nome} removida com sucesso!')
        else:
            print('Sem conexão com servidor.')

    def somar_gasto_cat(self, mes, categoria):
        if self.conexao.is_connected():
            sql = f"SELECT SUM({categoria}) FROM valor WHERE mes = {mes};"
            self.cursor.execute(sql)
            for c1 in self.cursor:
                return c1


class Compra:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def adicionar_valor(self, valor, mes, categoria, total_compra=0):
        if self.conexao.is_connected():
            if total_compra != 0:
                sql = 'INSERT INTO valor (registro, mes, compra_total, categoria, ano) VALUES ("{}", "{}", "{}", "{}", "{} ")'\
                    .format(valor, mes, total_compra, categoria, ano.year)
                self.cursor.execute(sql)
                self.conexao.commit()
            else:
                sql = 'INSERT INTO valor (registro, mes, categoria, ano) VALUES ("{}", "{}", "{}", "{}")' \
                    .format(valor, mes, categoria, ano.year)
                self.cursor.execute(sql)
                self.conexao.commit()
                print('Valor inserido com sucesso!')
        else:
            print('Sem conexão com o servidor.')

    def alterar_valor(self, novo_valor, id_valor, total_compra=''):
        if self.conexao.is_connected():
            if total_compra == '':
                sql = 'UPDATE valor SET registro = "{}" WHERE id_valor = "{}"'.format(novo_valor, id_valor)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Novo valor para a compra ID {id_valor} alterado para R${novo_valor}.')
            else:
                sql = 'UPDATE valor SET registro = "{}" WHERE total_compra = "{}"'.format(novo_valor, total_compra)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Valor alterado para todas as parcelas vinculadas, sendo R${novo_valor} para cada uma.')
        else:
            print('Sem conexão com servidor.')

    def deletar_valor(self, id_valor):
        if self.conexao.is_connected():
            sql = f'DELETE FROM valor WHERE id_valor = {id_valor}'
            self.cursor.execute(sql)
            self.conexao.commit()
            print(f'Valor de id {id_valor} removido com sucesso.')

    def adicionar_compra_p(self, total_compra, parcelas):
        if self.conexao.is_connected():
            sql = 'INSERT INTO total_compra (compra, t_parcela) VALUES ("{}", "{}")' \
                .format(total_compra, parcelas)
            self.cursor.execute(sql)
            self.conexao.commit()
        else:
            print('Sem conexão com o servidor.')

    def remover_compra_p(self, id_compra):
        if self.conexao.is_connected():
            sql = f'DELETE FROM valor WHERE compra_total = {id_compra}'
            sql2 = f'DELETE FROM total_compra WHERE id_compra = {id_compra}'
            self.cursor.execute(sql)
            self.conexao.commit()
            self.cursor.execute(sql2)
            self.conexao.commit()
            print('Compra retirada com sucesso.')
        else:
            print('Erro no servidor.')

    def somar_gasto(self, mes):
        if self.conexao.is_connected():
            sql = f"SELECT SUM(registro) FROM valor WHERE mes = {mes};"
            self.cursor.execute(sql)
            for c1 in self.cursor:
                return c1
        else:
            print('Sem conexão com servidor.')


class SalarioRendimento:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def inserir_salario(self, salario, mes):
        if self.conexao.is_connected():
            sql = 'INSERT INTO salario (pagamento, mes, ano) VALUES ("{}", "{}", "{}")'.format(salario, mes, ano.year)
            self.cursor.execute(sql)
            self.conexao.commit()
            print('Salario inserido com sucesso!')
        else:
            print('Sem conexão com o servidor.')

    def alterar_salario(self, salario, id_sal):
        if self.conexao.is_connected():
            sql = 'UPDATE salario SET pagamento = "{}" WHERE id_sal = "{}"'.format(salario, id_sal)
            self.cursor.execute(sql)
            self.conexao.commit()
            print('Salário alterado com sucesso!')
        else:
            print('Sem conexão com servidor.')

    def deletar_salario(self, id_sal):
        if self.conexao.is_connected():
            sql = f'DELETE FROM salario WHERE id_sal = {id_sal}'
            self.cursor.execute(sql)
            self.conexao.commit()
            print('Salário deletado com sucesso!')
        else:
            print('Sem conexão com servidor.')

    def inserir_rendimento(self, rendimento, mes):
        if self.conexao.is_connected():
            sql = 'INSERT INTO rendimento (valor, mes, ano) VALUES ("{}", "{}", "{}")'.format(rendimento, mes, ano.year)
            self.cursor.execute(sql)
            self.conexao.commit()
            print('Rendimento (valor extra) inserido com sucesso!')
        else:
            print('Sem conexão com o servidor.')

    def alterar_rendimento(self, rendimento, id_red):
        if self.conexao.is_connected():
            sql = 'UPDATE salario SET valor = "{}" WHERE id_red = "{}"'.format(rendimento, id_red)
            self.cursor.execute(sql)
            self.conexao.commit()
            print('Rendimento (valor extra) alterado com sucesso!')
        else:
            print('Sem conexão com servidor.')

    def deletar_rendimento(self, id_red):
        if self.conexao.is_connected():
            sql = f'DELETE FROM rendimento WHERE id_red = {id_red}'
            self.cursor.execute(sql)
            self.conexao.commit()
            print('Rendimento (valor extra) deletado com sucesso!')
        else:
            print('Sem conexão com servidor.')
