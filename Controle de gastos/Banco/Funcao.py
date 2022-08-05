from .Ajustes import limpa_tela, valida_float, valida_int
from .Bd import Conector


def continuar(giros, mensagem):
    if giros > 0:
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
                     'Devido as tentativas sem sucesso, a opção de inserir compra foi fechada.', 10)
    if mes == 0:
        return 0
    elif mes >= 13:
        print('Valor não corresponde a nenhum mês.')
        limpa_tela()
    else:
        limpa_tela(0)
        return mes


def apresentar_compras(con, mes):
    conexao = con
    if conexao.is_connected():
        sql = f'SELECT DISTINCT V.id_valor, V.registro, C.compra, CA.nome FROM valor V INNER JOIN total_compra C ' \
              f'ON V.compra_total = C.id_compra INNER JOIN categoria CA ON V.categoria = CA.id_cat WHERE V.mes = {mes};'
        cursor = conexao.cursor()
        cursor.execute(sql)
        print('ID\t Valor\t Total da compra(caso parcelada)\tCategoria')
        for c1, c2, c3, c4 in cursor:
            print(f'{c1}\tR${c2}\t \t\t\t\t\t\tR${c3}\t\t\t{c4}')

