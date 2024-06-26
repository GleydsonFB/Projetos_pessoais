import datetime
import sqlite3

data = datetime.datetime.now()
ano = data.date()


class Conector:
    def __init__(self):
        self.conexao = None
        self.cursor = None

    def conectar(self):
        self.conexao = sqlite3.connect('base_cf.db')
        self.cursor = self.conexao.cursor()
        return self.conexao

    def desconectar(self):
        self.conexao.close()

    def criar_auxiliares(self):
        sql = 'SELECT * FROM mes;'
        return_sql = []
        self.cursor.execute(sql)
        for item in self.cursor:
            return_sql.append(item)
        if len(return_sql) > 0:
            pass
        else:
            self.cursor.execute('INSERT INTO mes (id_mes, nome) VALUES (1, "Janeiro");')

            self.cursor.execute('INSERT INTO mes (id_mes, nome) VALUES (2, "Fevereiro");')

            self.cursor.execute('INSERT INTO mes (id_mes, nome) VALUES (3, "Março");')

            self.conexao.commit()

        sql = 'SELECT compra, t_parcela FROM total_compra WHERE id_compra = 1;'
        return_sql = []
        self.cursor.execute(sql)
        for item in self.cursor:
            return_sql.append(item)
        if len(return_sql) > 0:
            if return_sql[0][0] == 0:
                pass
            else:
                self.cursor.execute('UPDATE total_compra SET compra = 0 WHERE id_compra = 1;')

                self.cursor.execute('UPDATE total_compra SET t_parcela = 0 WHERE id_compra = 1;')

                self.conexao.commit()

        else:
            self.cursor.execute('INSERT INTO total_compra (id_compra, compra, t_parcela) VALUES (1, 0, 0);')
            self.conexao.commit()
                    
    def criar_tabelas(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS categoria"
                            "(id_cat INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
                            "nome VARCHAR(255) NOT NULL,"
                            "limite_gasto DECIMAL(10,2) NOT NULL,"
                            "minimo_gasto DECIMAL(10,2) NULL DEFAULT 0)")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS mes"
                            "(id_mes INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
                            "nome VARCHAR(45) NOT NULL)")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS rendimento"
                            "(id_red INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
                            "valor DECIMAL(10,2) NOT NULL,"
                            "mes INTEGER NOT NULL,"
                            "ano INTEGER NOT NULL,"
                            "FOREIGN KEY (mes) REFERENCES mes(id_mes))")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS salario"
                            "(id_sal INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
                            "pagamento DECIMAL(10,2) NOT NULL,"
                            "mes INTEGER NOT NULL,"
                            "ano INTEGER NOT NULL,"
                            "FOREIGN KEY (mes) REFERENCES mes(id_mes))")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS total_compra"
                            "(id_compra INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
                            "compra DECIMAL(10,2) NOT NULL,"
                            "t_parcela INTEGER NOT NULL)")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS valor"
                            "(id_valor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
                            "registro DECIMAL(10,2) NOT NULL, mes INTEGER NOT NULL,"
                            "compra_total INTEGER NULL DEFAULT 1,"
                            "categoria INTEGER NOT NULL,"
                            "ANO INTEGER NOT NULL,"
                            "nome_compra VARCHAR(100) NULL DEFAULT 'N/A',"
                            "FOREIGN KEY (mes) REFERENCES mes(id_mes),"
                            "FOREIGN KEY (compra_total) REFERENCES total_compra(id_compra),"
                            "FOREIGN KEY (categoria) REFERENCES categoria(id_cat))")

    def select_ultimo(self, nome_id, tabela):
        if self.conexao is not None:
            sql = f'SELECT MAX({nome_id}) FROM {tabela}'
            self.cursor.execute(sql)
            for c1 in self.cursor:
                return c1
        else:
            print('Sem conexão com o servidor.')

    def somar_gasto_compra(self, mes, an=ano.year):
        if self.conexao is not None:
            sql = f'SELECT SUM(registro) FROM valor WHERE mes = {mes} AND ano = {an}'
            self.cursor.execute(sql)
        for c1 in self.cursor:
            return c1

    def select_simples(self, coluna1, coluna2, tabela):
        if self.conexao is not None:
            sql = f"SELECT {coluna1}, {coluna2} FROM {tabela};"
            retorno = []
            self.cursor.execute(sql)
            for c1, c2 in self.cursor:
                retorno.append(c1)
                retorno.append(c2)
            return retorno
        else:
            print('Sem conexão com o servidor.')

    def select_simples_1col(self, tabela, coluna):
        if self.conexao is not None:
            sql = f"SELECT {coluna} FROM {tabela};"
            retorno = []
            self.cursor.execute(sql)
            for c1 in self.cursor:
                retorno.append(c1)
            return retorno
        else:
            print('Sem conexão com o servidor.')

    def select_composto(self, total_colunas, tabela, coluna1, colunap, pesquisa, *demais_colunas):
        if self.conexao is not None:
            match total_colunas:
                case 0:
                    sql = f'SELECT {coluna1} FROM {tabela} WHERE {colunap} = "{pesquisa}"'
                    self.cursor.execute(sql)
                    for c1 in self.cursor:
                        return c1
                case 1:
                    sql = f"SELECT {coluna1} FROM {tabela} WHERE {colunap} = {pesquisa}"
                    self.cursor.execute(sql)
                    for c1 in self.cursor:
                        return c1
                case 2:
                    sql = f"SELECT {coluna1}, {demais_colunas[0]} FROM {tabela} WHERE {colunap} = {pesquisa};"
                    self.cursor.execute(sql)
                    retorno = []
                    for c1, c2 in self.cursor:
                        retorno.append(c1)
                        retorno.append(c2)
                    return retorno
                case 3:
                    sql = \
                        f"SELECT {coluna1}, {demais_colunas[0]}, {demais_colunas[1]} FROM {tabela} WHERE {colunap} = {pesquisa};"
                    self.cursor.execute(sql)
                    retorno = []
                    for c1, c2, c3 in self.cursor:
                        retorno.append(c1)
                        retorno.append(c2)
                        retorno.append(c3)
                    return retorno
                case 4:
                    sql = \
                        f"SELECT {coluna1}, {demais_colunas[0]}, {demais_colunas[1]}, {demais_colunas[2]} FROM {tabela} WHERE {colunap} = {pesquisa};"
                    self.cursor.execute(sql)
                    retorno = []
                    for c1, c2, c3, c4 in self.cursor:
                        retorno.append(c1)
                        retorno.append(c2)
                        retorno.append(c3)
                        retorno.append(c4)
                    return retorno
                case 5:
                    sql = \
                        f"SELECT * FROM {tabela} WHERE {colunap} = {pesquisa};"
                    self.cursor.execute(sql)
                    retorno = []
                    for c1, c2, c3, c4, c5 in self.cursor:
                        retorno.append(c1)
                        retorno.append(c2)
                        retorno.append(c3)
                        retorno.append(c4)
                        retorno.append(c5)
                    return retorno
        else:
            print('Sem conexão com servidor.')


class Categoria:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def inserir_categoria(self, nome, limite, minimo=0):
        if self.conexao is not None:
            if minimo != 0:
                sql = 'INSERT INTO categoria (nome, limite_gasto, minimo_gasto) VALUES ("{}", "{}", "{}")'.format(nome,
                                                                                                                  limite,
                                                                                                                  minimo)
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
        if self.conexao is not None:
            if nome != '' and limite == '' and minimo == '':
                sql = 'UPDATE categoria SET nome = "{}" WHERE id_cat = "{}"'.format(nome, id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Novo nome da categoria definido como {nome}!')
            elif nome != '' and limite != '' and minimo == '':
                sql = 'UPDATE categoria SET nome = "{}", limite_gasto = "{}" WHERE id_cat = "{}"'.format(nome, limite,
                                                                                                         id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Alterado nome e limite para: {nome} e {limite}!')
            elif nome != '' and limite != '' and minimo != '':
                sql = 'UPDATE categoria SET nome = "{}", limite_gasto = "{}", minimo_gasto = "{}" WHERE id_cat = "{}"'.format(
                    nome, limite, minimo, id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Alterado nome, limite e minimo gasto para: {nome}, R${limite} e R${minimo}!')
            elif nome == '' and limite != '' and minimo == '':
                sql = 'UPDATE categoria SET limite_gasto = "{}" WHERE id_cat = "{}"'.format(limite, id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Novo limite definido para R${limite}!')
            elif nome == '' and limite != '' and minimo != '':
                sql = 'UPDATE categoria SET limite_gasto = "{}", minimo_gasto = "{}" WHERE id_cat = "{}"'.format(limite,
                                                                                                                 minimo,
                                                                                                                 id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Novo limite definido para R${limite} e mínimo de R${minimo}!')
            elif nome == '' and limite == '' and minimo != '':
                sql = 'UPDATE categoria SET minimo_gasto = "{}" WHERE id_cat = "{}"'.format(minimo, id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Novo valor mínimo definido para R${minimo}!')
            elif nome != '' and limite == '' and minimo != '':
                sql = 'UPDATE categoria SET nome = "{}", minimo_gasto = "{}" WHERE id_cat = "{}"'.format(nome, minimo,
                                                                                                         id_cat)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Nome alterado para {nome} e com novo valor mínimo de R${minimo}!')
            else:
                print('Opção inválida.')
        else:
            print('Sem conexão com o servidor.')

    def somar_gasto_cat(self, mes, categoria):
        if self.conexao is not None:
            sql = f"SELECT SUM(registro) FROM valor WHERE mes = {mes} AND categoria = {categoria} AND ano = {ano.year};"
            self.cursor.execute(sql)
            for c1 in self.cursor:
                return c1
        else:
            print('Sem conexão com o servidor.')


class Compra:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def adicionar_valor(self, valor, mes, categoria, an=ano.year, nome_compra='', total_compra=0):
        if self.conexao is not None:
            if total_compra != 0 and nome_compra != '':
                sql = 'INSERT INTO valor (registro, mes, compra_total, categoria, ano, nome_compra) VALUES ("{}", "{}", "{}", "{}", "{}", "{}")' \
                    .format(valor, mes, total_compra, categoria, an, nome_compra)
                self.cursor.execute(sql)
                self.conexao.commit()
            elif total_compra != 0 and nome_compra == '':
                sql = 'INSERT INTO valor (registro, mes, compra_total, categoria, ano) VALUES ("{}", "{}", "{}", "{}", "{}")' \
                    .format(valor, mes, total_compra, categoria, an)
                self.cursor.execute(sql)
                self.conexao.commit()
            elif total_compra == 0 and nome_compra != '':
                sql = 'INSERT INTO valor (registro, mes, categoria, ano, nome_compra) VALUES ("{}", "{}", "{}", "{}", "{}")' \
                    .format(valor, mes, categoria, an, nome_compra)
                self.cursor.execute(sql)
                self.conexao.commit()
            else:
                sql = 'INSERT INTO valor (registro, mes, categoria, ano) VALUES ("{}", "{}", "{}", "{}")' \
                    .format(valor, mes, categoria, an)
                self.cursor.execute(sql)
                self.conexao.commit()
        else:
            print('Sem conexão com o servidor.')

    def alterar_valor(self, novo_valor, id_valor, total_compra=0, novo_valorc=0):
        if self.conexao is not None:
            if total_compra == 0:
                sql = 'UPDATE valor SET registro = "{}" WHERE id_valor = "{}"'.format(novo_valor, id_valor)
                self.cursor.execute(sql)
                self.conexao.commit()
                print(f'Novo valor para a compra ID {id_valor} alterado para R${novo_valor:.2f}.')
            else:
                sql = 'UPDATE valor SET registro = "{}" WHERE compra_total = "{}";'.format(novo_valor, total_compra)
                sql2 = 'UPDATE total_compra SET compra = "{}" WHERE id_compra = "{}"'.format(novo_valorc, total_compra)
                self.cursor.execute(sql)
                self.conexao.commit()
                self.cursor.execute(sql2)
                self.conexao.commit()
                print(f'Valor alterado para todas as parcelas vinculadas, sendo R${novo_valor:.2f} '
                      f'para cada uma e o total da compra é de R${novo_valorc:.2f}.')
        else:
            print('Sem conexão com servidor.')

    def deletar_valor(self, id_valor):
        if self.conexao is not None:
            sql = f'DELETE FROM valor WHERE id_valor = {id_valor}'
            self.cursor.execute(sql)
            self.conexao.commit()
            print(f'Valor de id {id_valor} removido com sucesso.')
        else:
            print('Sem conexão com o servidor.')

    def deletar_valor_mes(self, mes, ano_del, id_compra):
        if self.conexao is not None:
            sql = f'DELETE FROM valor WHERE mes = {mes} AND ano = {ano_del} AND compra_total = {id_compra}'
            self.cursor.execute(sql)
            self.conexao.commit()
        else:
            print('Sem conexão com servidor.')

    def remover_compras_r(self, mes_atual, ano_atual, id_compra):
        if self.conexao is not None:
            sql = f'DELETE FROM valor WHERE compra_total = {id_compra} AND mes >= {mes_atual} AND ano >= {ano_atual}'
            self.cursor.execute(sql)
            self.conexao.commit()
            print('Todas as compras futuras atreladas (incluindo o mês informado) foram apagadas!')
        else:
            print('Sem conexão com servidor.')

    def adicionar_compra_p(self, total_compra, parcelas):
        if self.conexao is not None:
            sql = 'INSERT INTO total_compra (compra, t_parcela) VALUES ("{}", "{}")' \
                .format(total_compra, parcelas)
            self.cursor.execute(sql)
            self.conexao.commit()
        else:
            print('Sem conexão com o servidor.')

    def remover_compra_p(self, id_compra):
        if self.conexao is not None:
            sql = f'DELETE FROM valor WHERE compra_total = {id_compra}'
            sql2 = f'DELETE FROM total_compra WHERE id_compra = {id_compra}'
            self.cursor.execute(sql)
            self.conexao.commit()
            self.cursor.execute(sql2)
            self.conexao.commit()
            print('Compra removida de todos os meses atrelados.')
        else:
            print('Erro no servidor.')

    def antecipar_compra_p(self, id_compra, mes_atual, ano_atual, total_ante):
        if self.conexao is not None:
            sql = f'SELECT V.ano FROM valor V INNER JOIN total_compra T ON V.compra_total = T.id_compra WHERE V.compra_total = {id_compra}'
            sql2 = f'SELECT MIN(V.mes) as mes, MIN(V.ano) as ano FROM valor V INNER JOIN total_compra T ON V.compra_total = T.id_compra WHERE V.compra_total = {id_compra}'
            parcelas = []
            ano_inicial, mes_inicial = '', ''
            self.cursor.execute(sql)
            for c1 in self.cursor:
                parcelas.append(c1)
            total_parcelas = len(parcelas)
            self.cursor.execute(sql2)
            for c1, c2 in self.cursor:
                mes_inicial = c1
                ano_inicial = c2
            if ano_atual - ano_inicial > 1:
                conta = (ano_atual - ano_inicial) * 12
                conta = conta - mes_inicial
                parcelas_pagas = conta + mes_atual
            elif ano_atual - ano_inicial == 1:
                parcelas_pagas = (12 - mes_inicial) + mes_atual
            elif ano_atual - ano_inicial < 0:
                return print('Opção inválida.')
            else:
                parcelas_pagas = mes_atual - mes_inicial
                if parcelas_pagas < 0:
                    return print('Não é possível antecipar uma compra que não teve seu início ainda.')
                else:
                    pass
            parcelas_restantes = total_parcelas - parcelas_pagas
            if total_ante > parcelas_restantes:
                return print('Não é possível antecipar mais parcelas do que o restante.')
            elif total_ante - parcelas_restantes == 1:
                return print('Só falta uma parcela, então não tem como antecipar.')
            else:
                for registro in range(total_ante):
                    id_del = 0
                    sql3 = f'SELECT id_valor FROM valor WHERE id_valor AND compra_total = {id_compra} ORDER BY id_valor DESC LIMIT 1'
                    self.cursor.execute(sql3)
                    for c1 in self.cursor:
                        id_del = c1
                    sql4 = f'DELETE FROM valor WHERE id_valor = {id_del[0]}'
                    self.cursor.execute(sql4)
                    self.conexao.commit()
                print(f'Foram antecipadas {total_ante} parcelas com sucesso!')
                return total_ante
        else:
            print('Erro no servidor.')

    def somar_gasto(self, mes):
        if self.conexao is not None:
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

    def inserir_salario(self, salario, mes, an=ano.year):
        if self.conexao is not None:
            sql = 'INSERT INTO salario (pagamento, mes, ano) VALUES ("{}", "{}", "{}")'.format(salario, mes, an)
            self.cursor.execute(sql)
            self.conexao.commit()
            print('Salario inserido com sucesso!')
        else:
            print('Sem conexão com o servidor.')

    def alterar_salario(self, salario, id_sal):
        if self.conexao is not None:
            sql = 'UPDATE salario SET pagamento = "{}" WHERE id_sal = "{}"'.format(salario, id_sal)
            self.cursor.execute(sql)
            self.conexao.commit()
            print('Salário alterado com sucesso!')
        else:
            print('Sem conexão com servidor.')

    def deletar_salario(self, id_sal):
        if self.conexao is not None:
            sql = f'DELETE FROM salario WHERE id_sal = {id_sal}'
            self.cursor.execute(sql)
            self.conexao.commit()
            print('Salário deletado com sucesso!')
        else:
            print('Sem conexão com servidor.')

    def inserir_rendimento(self, rendimento, mes, an=ano.year):
        if self.conexao is not None:
            sql = 'INSERT INTO rendimento (valor, mes, ano) VALUES ("{}", "{}", "{}")'.format(rendimento, mes, an)
            self.cursor.execute(sql)
            self.conexao.commit()
            print('Rendimento (valor extra) inserido com sucesso!')
        else:
            print('Sem conexão com o servidor.')

    def alterar_rendimento(self, rendimento, id_red):
        if self.conexao is not None:
            sql = 'UPDATE rendimento SET valor = "{}" WHERE id_red = "{}"'.format(rendimento, id_red)
            self.cursor.execute(sql)
            self.conexao.commit()
            print('Rendimento (valor extra) alterado com sucesso!')
        else:
            print('Sem conexão com servidor.')

    def deletar_rendimento(self, id_red):
        if self.conexao is not None:
            sql = f'DELETE FROM rendimento WHERE id_red = {id_red}'
            self.cursor.execute(sql)
            self.conexao.commit()
            print('Rendimento (valor extra) deletado com sucesso!')
        else:
            print('Sem conexão com servidor.')
