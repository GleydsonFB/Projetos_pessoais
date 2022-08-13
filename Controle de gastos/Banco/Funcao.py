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
            sql = f'SELECT V.id_valor, V.registro, C.compra, CA.nome, V.ano FROM valor V INNER JOIN total_compra C ' \
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
                print("ID\t Valor\t Total da compra(0 se não for)\tCategoria\tAno da compra")
                for c1, c2, c3, c4, c5 in cursor:
                    print(f'{c1}\t R${c2}\t\t\t\t\t\t\tR${c3}\t  {c4} \t\t{c5}')
                return execucao
        elif mostrar_id is False and ano != 'nenhum':
            sql = f'SELECT V.registro, C.compra, CA.nome, V.ano FROM valor V INNER JOIN total_compra C ' \
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
                print("Valor\t Total da compra(0 se não for)\tCategoria\tAno da compra")
                for c1, c2, c3, c4 in cursor:
                    print(f'R${c1}\t\t\t\t\t\t\tR${c2}\t  {c3} \t\t{c4}')
        else:
            sql = f'SELECT V.id_valor, V.registro, C.compra, CA.nome FROM valor V INNER JOIN total_compra C ' \
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
                print("ID\tValor\t Total da compra(0 se não for)\tCategoria")
                for c1, c2, c3, c4 in cursor:
                    print(f'{c1}\tR${c2}\t\t\t\t\t\t\tR${c3}\t  {c4}')
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
            print(f'ID\t\tPAGAMENTO\t\tANO')
            for c1, c2, c3 in cursor:
                print(f'{c1}\t\tR${c2}\t\t{c3}')
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
            print(f'ID\t\tVALOR\t\tANO')
            for c1, c2, c3 in cursor:
                print(f'{c1}\t\tR${c2}\t\t{c3}')
            return ides


def apresentar_categorias(con):
    conexao = con
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
            print(f'ID\t\tNOME\t\tLIMITE\t\tGASTO MIN')
            for c1, c2, c3, c4 in cursor:
                print(f'{c1}\t\t{c2}\t\tR${c3}\t\t  R${c4}')
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


