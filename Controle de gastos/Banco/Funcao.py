from .Ajustes import limpa_tela, valida_float, valida_int
from .Bd import Conector


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
    if conexao.is_connected():
        if mostrar_id is True and ano != 'nenhum':
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
                    print(f'ID:{c1}\tValor: R${c2}\t\tTotal da compra (0 se não for parcelada): R${c3}\tCategoria: {c4}\tAno: {c5}\tNome da compra: {c6}.')
                print('\n')
                return execucao
        elif mostrar_id is False and ano != 'nenhum':
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
                    print(f'Valor: R${c1}\t\tTotal da compra(0 se não for parcelada): R${c2}\t  Categoria: {c3}\tAno: {c4}\tNome da compra: {c5}.')
                return execucao
        else:
            sql = f'SELECT V.id_valor, V.registro, C.compra, CA.nome, V.nome_compra FROM valor V INNER JOIN total_compra C ' \
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
                for c1, c2, c3, c4, c5 in cursor:
                    print(f'ID:{c1}\tValor: R${c2}\t\tTotal da compra (0 se não for parcelada): R${c3}\t  Categoria: {c4}\tNome da compra: {c5}.')
                return execucao
    else:
        print('Sem conexão com servidor.')


def apresentar_salarios(con, mes, gasto=False):
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
                print(f'ID:{c1}\t\tSalário: R${c2}\t\tAno: {c3}')
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
            for c1, c2, c3 in cursor:
                print(f'ID:{c1}\t\tValor: R${c2}\t\tAno: {c3}')
            return ides


def apresentar_categorias(con):
    conexao = con
    tamanho = []
    tamanho2 = []
    if conexao.is_connected():
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
            cursor.execute(sql)
            print('\nSegue os dados das atuais categorias:\n')
            for c1, c2, c3, c4 in cursor:
                print(f'ID: {c1}\tNome: {c2}\t\tLimite: R${c3}\t\tGasto mínimo: R${c4}.')
            return ides


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


def estatistica_compras(con, mes, ano):
    conexao = con
    if conexao.is_connected():
        sql = f'SELECT V.registro, C.compra, CA.nome, V.ano, V.nome_compra FROM valor V INNER JOIN total_compra C ' \
              f'ON V.compra_total = C.id_compra INNER JOIN categoria CA ON V.categoria = CA.id_cat WHERE V.mes = {mes} AND V.ano = {ano};'
        cursor = conexao.cursor()
        cursor.execute(sql)
        sql2 = f'SELECT pagamento FROM salario WHERE mes = {mes} AND ano = {ano}'
        sql3 = f'SELECT valor FROM rendimento WHERE mes = {mes} AND ano = {ano}'
        total_gastol = []
        total_gasto, salario, rendimento = 0, 0, 0
        for valor in cursor:
            total_gastol.append(valor[0])
        for valor in total_gastol:
            total_gasto += total_gastol[valor]
        print('\nConfira os detalhes abaixo:\n')
        for c1, c2, c3, c4, c5 in cursor:
            print(f'ID:{c1}\tValor: R${c2}\t\tTotal da compra (0 se não for parcelada): R${c3}\t  Categoria: {c4}\tNome da compra: {c5}.')
        print(f'\nTotal gasto no mês até o momento: R${total_gasto}')
        cursor.execute(sql2)
        

