from .Ajustes import limpa_tela, valida_float, valida_int
from .Bd import Conector
import datetime
data = datetime.datetime.now()
ano = data.date()
from prettytable import PrettyTable


def continuar(contagem, mensagem):
    if contagem > 0:
        print(f'Deseja {mensagem}')
        novo = str(input('[S/N]: '))
        while novo not in 'SsNn':
            novo = str(input('Digite [S/N]: '))
        if novo in 'Ss':
            return 1
        else:
            limpa_tela(0)
            return 0


def escolher_mes():
    while True:
        mes = valida_int('Digite o mês correspondente: ', 'Opção inválida',
                         'Devido as tentativas sem sucesso, a opção foi fechada.', 10)
        if mes == 0:
            return 0
        elif mes >= 13:
            print('Valor não corresponde a nenhum mês.')
            limpa_tela()
        else:
            limpa_tela(0)
            return mes


def apresentar_compras(con, mes, ano='nenhum', mostrar_id=False):
    conexao = con
    table = PrettyTable()
    if conexao.is_connected():
        if mostrar_id is True and ano != 'nenhum':
            table.field_names = ['ID', 'Valor', 'Total da compra (0 se não for parcelada)', 'Categoria', 'Ano', 'Nome da compra']
            sql = f'SELECT V.id_valor, V.registro, C.compra, CA.nome, V.ano, V.nome_compra FROM valor V INNER JOIN total_compra C ' \
                  f'ON V.compra_total = C.id_compra INNER JOIN categoria CA ON V.categoria = CA.id_cat WHERE V.mes = {mes} AND V.ano = {ano};'
            cursor = conexao.cursor()
            cursor.execute(sql)
            execucao = []
            for c1 in cursor:
                execucao.append(c1[0])
            if len(execucao) == 0:
                print('Não há valores para o mês inserido.')
                return 0
            else:
                cursor.execute(sql)
                print('\nConfira os detalhes abaixo:\n')
                for c1, c2, c3, c4, c5, c6 in cursor:
                    table.add_row([c1, f"R${c2}", f"R${c3}", c4, c5, c6])
                print(table)
                return execucao
        elif mostrar_id is False and ano != 'nenhum':
            table.field_names = ['Valor', 'Total da compra (0 se não for parcelada)', 'Categoria', 'Ano', 'Nome da compra']
            sql = f'SELECT V.registro, C.compra, CA.nome, V.ano, V.nome_compra FROM valor V INNER JOIN total_compra C ' \
                  f'ON V.compra_total = C.id_compra INNER JOIN categoria CA ON V.categoria = CA.id_cat WHERE V.mes = {mes} AND V.ano = {ano};'
            cursor = conexao.cursor()
            cursor.execute(sql)
            execucao = []
            for c1 in cursor:
                execucao.append(c1[0])
            if len(execucao) == 0:
                print('Não há valores para o mês inserido.')
                return 0
            else:
                cursor.execute(sql)
                print('\nConfira os dados abaixo:\n')
                for c1, c2, c3, c4, c5 in cursor:
                    table.add_row([f'R${c1}', f'R${c2}', c3, c4, c5])
                print(table)
                return execucao
        else:
            table.field_names = ['ID', 'Valor', 'Total da compra (0 se não for parcelada)', 'Categoria', 'Ano', 'Nome da compra']
            sql = f'SELECT V.id_valor, V.registro, C.compra, CA.nome, V.ano, V.nome_compra FROM valor V INNER JOIN total_compra C ' \
                  f'ON V.compra_total = C.id_compra INNER JOIN categoria CA ON V.categoria = CA.id_cat WHERE V.mes = {mes};'
            cursor = conexao.cursor()
            cursor.execute(sql)
            execucao = []
            for c1 in cursor:
                execucao.append(c1[0])
            if len(execucao) == 0:
                print('Não há valores para o mês inserido.')
                return 0
            else:
                cursor.execute(sql)
                print('\nConfira os detalhes abaixo:\n')
                for c1, c2, c3, c4, c5, c6 in cursor:
                    table.add_row([c1, f'R${c2}', f'R${c3}', c4, c5, c6])
                print(table)
                return execucao
    else:
        print('Sem conexão com servidor.')


def apresentar_salarios(con, mes, gasto=False):
    table = PrettyTable()
    table.field_names = ['ID', 'Salário', 'Ano']
    conexao = con
    if conexao.is_connected():
        sql = f'SELECT id_sal, pagamento, ano FROM salario WHERE mes = {mes}'
        cursor = conexao.cursor()
        cursor.execute(sql)
        ides = []
        for c1 in cursor:
            ides.append(c1[0])
        if len(ides) == 0:
            print('Não há salários para o intervalo selecionado.')
            return 0
        else:
            cursor.execute(sql)
            print(f'\nConfira os detalhes abaixo:\n')
            for c1, c2, c3 in cursor:
                table.add_row([c1, f'R${c2}', c3])
            print(table)
            return ides


def apresentar_rendimentos(con, mes, gasto=False):
    conexao = con
    if conexao.is_connected():
        sql = f'SELECT id_red, valor, ano FROM rendimento WHERE mes = {mes}'
        cursor = conexao.cursor()
        cursor.execute(sql)
        ides = []
        for c1 in cursor:
            ides.append(c1[0])
        if len(ides) == 0:
            print('Não há rendimentos para o intervalo selecionado.')
            return 0
        else:
            cursor.execute(sql)
            print('\nconfira os detalhes abaixo:\n')
            table = PrettyTable()
            table.field_names = ['ID', 'Valor', 'Ano']
            for c1, c2, c3 in cursor:
                table.add_row([c1, c2, c3])
            print(table)
            return ides


def apresentar_categorias(con, nome='nenhum', mes=ano.month, an=ano.year):
    conexao = con
    ide = 0
    table = PrettyTable()
    if conexao.is_connected():
        if nome == 'nenhum':
            sql = 'SELECT id_cat, nome, limite_gasto, minimo_gasto FROM categoria;'
            cursor = conexao.cursor()
            cursor.execute(sql)
            ides = []
            for c1 in cursor:
                ides.append(c1[0])
            if len(ides) == 0:
                print('Não há categorias cadastradas.')
                return 0
            else:
                table.field_names = ['ID', 'Nome', 'Limite', 'Gasto mínimo']
                cursor.execute(sql)
                print('\nSegue os dados das atuais categorias:\n')
                for c1, c2, c3, c4 in cursor:
                    table.add_row([c1, c2, f'R${c3}', f'R${c4}'])
                print(table)
                return ides
        else:
            listagem = []
            sql = f'SELECT id_cat FROM categoria WHERE nome = "{nome}"'
            cursor = conexao.cursor()
            cursor.execute(sql)
            for c1 in cursor:
                ide = c1
                break
            sql2 = f'SELECT SUM(registro) FROM valor WHERE categoria = {ide[0]} AND ano = {an} AND mes = {mes}'
            cursor.execute(sql2)
            for c1 in cursor:
                listagem.append(c1)
            sql3 = f'SELECT V.registro, V.nome_compra, C.compra, V.ano  FROM valor V INNER JOIN total_compra C ON V.compra_total = C.id_compra ' \
                   f'WHERE categoria = {ide[0]} AND ano = {an} AND mes = {mes}'
            cursor.execute(sql3)
            if listagem[0][0] is None:
                print('Não há gastos para o período selecionado.')
                limpa_tela()
                return 0
            else:
                table.field_names = ['Valor', 'Nome da compra', 'Total da compra(0 se não for parcelada)']
                print(f'Confira os detalhes de gasto da categoria {nome} para o {mes}° mês de {an} abaixo:')
                for c1, c2, c3, c4 in cursor:
                    table.add_row([f'R${c1}', c2, f'R${c3}'])
                print(table)
                return listagem
    else:
        print('Sem conexão com o servidor.')


def escolher_compra_edit(con, ide, lista_id):
    conexao = con
    if conexao.is_connected():
        local = valida_int(ide, 'Digite um número inteiro', '')
        if local not in lista_id:
            print('ID digitado não está presente na selação. \nRetornando ao menu anterior.')
            return 'n'
        else:
            return local
    else:
        print('Sem conexão com servidor.')


def rendimentos_totais_mes_a(con, mes, an=ano.year):
    conexao = con
    totais = []
    if conexao.is_connected():
        sql = f'SELECT SUM(pagamento) FROM salario WHERE mes = {mes} AND ano = {an}'
        cursor = conexao.cursor()
        cursor.execute(sql)
        for c1 in cursor:
            totais.append(c1)
        sql2 = f'SELECT SUM(valor) FROM rendimento WHERE mes = {mes} AND ano = {an}'
        cursor.execute(sql2)
        for c1 in cursor:
            totais.append(c1)
        return totais
    else:
        print('Sem conexão com o servidor.')