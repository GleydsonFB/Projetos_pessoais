from Banco import Bd
from Banco import Ajustes
from time import sleep

bd = Bd.Conector('localhost', 'root', 'root', 'controle_de_gastos')
conexao = bd.conectar()
categorias = Bd.Categoria(conexao)
compras = Bd.Compra(conexao)
contador, verificador = 0, 0
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
while True:
    print('BEM VINDO(A) AO CONTROLE FINANCEIRO PESSOAL - by Gleydson\n'
          'DEFINA UMA DAS OPÇÕES ABAIXO:')
    menu = Ajustes.valida_int('[1] GERIR COMPRAS - [2] GERIR SALARIO - [3] GERIR RENDIMENTO - [4] GERIR CATEGORIA: ',
                              'Digite um número inteiro',
                              'Devido as tentativas sem sucesso, o programa será encerrado...', 2)
    match menu:
        case 0:
            break
        case 1:
            Ajustes.limpa_tela()
            print('Nesta seção temos as opções para lidar com compras')
            escolha = Ajustes.valida_int('O que você deseja?\n'
                                         '[1] INSERIR COMPRA - [2] - ALTERAR COMPRA - [3] - DELETAR COMPRA: ',
                                         'Digite um valor válido.', 10)
            if escolha == 1:
                while True:
                    print('Certo, primeiro determine o mês que irá conter a compra: ')
                    Ajustes.apresenta_mes()
                    mes = Ajustes.valida_int('Digite o mês correspondente: ', 'Opção inválida',
                                             'Devido as tentativas sem sucesso, a opção de inserir compra foi fechada.', 10)
                    if mes == 0:
                        break
                    elif mes >= 13:
                        print('Valor não corresponde a nenhum mês.')
                        sleep(2)
                        Ajustes.limpa_tela()
                    else:
                        Ajustes.limpa_tela()
                        print(f'A compra será inserida no mês {meses[mes - 1]}')
                        ver_cat = bd.select_simples('id_cat', 'nome', 'categoria')
                        if len(ver_cat) > 0:
                            print('Escolha a categoria que a compra será inserida!')
                            for dado, tup in enumerate(ver_cat):
                                if dado + 1 < len(ver_cat):
                                    print(f'Código: {ver_cat[dado]} --- {ver_cat[dado + 1]}.')
                                else:
                                    break
                        escolha_cat = Ajustes.valida_int('Digite o código da categoria desejada', 'Opção inválida.',
                                                         'Tentativas encerradas, retornando ao menu anterior', 10)
                        if escolha_cat == 0:
                            break
                        elif escolha_cat > (len(ver_cat) / 2):
                            print('Opção não corresponde a nenhuma categoria.')
                            sleep(2)
                            Ajustes.limpa_tela()
                        else:
                            tipo_compra = Ajustes.valida_int('A compra será parcelada[1] ou à vista[2]? ', 'Opção inválida',
                                                             'Devido as tentativas sem sucesso, a opção retrocedeu', 10)
                            if tipo_compra == 0:
                                break
                            elif tipo_compra == 1:
                                limite = bd.select_composto(1, 'categoria', 'limite_gasto', 'id_cat', escolha_cat)
                                nome = bd.select_composto(1, 'categoria', 'nome', 'id_cat', escolha_cat)
                                gasto_atual = categorias.somar_gasto_cat(mes, escolha_cat)
                                if gasto_atual is None:
                                    pass
                                else:
                                    limite = limite[0] - gasto_atual[0]
                                valor = Ajustes.valida_float('Digite o valor da compra: ', 'Digite um número real.')
                                if valor > limite:
                                    print(f'O limite mensal da categoria {nome[0]} é de R${limite}.\n'
                                          f'A compra inserida ultrapassa esse valor...\n'
                                          f'Retornando ao menu inicial de compras.')
                                    sleep(3)
                                    break
                                else:
                                    parcela = Ajustes.valida_int('Digite a quantidade de parcelas', 'Digite um número inteiro', '')
                                    total_valor = valor * parcela
                                    compras.adicionar_compra_p(total_valor, parcela)
                                    

