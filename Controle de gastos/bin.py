from Banco import Bd, Ajustes, Funcao
import datetime
data = datetime.datetime.now()
ano = data.date()
an = int(ano.year)
bd = Bd.Conector('localhost', 'root', 'root', 'controle_de_gastos')
categorias = Bd.Categoria(bd.conectar())
compras = Bd.Compra(bd.conectar())
salarios = Bd.SalarioRendimento(bd.conectar())
contador, verificador = 0, 0
id_ultimo = bd.select_ultimo('id_compra', 'total_compra')
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
while True:
    print('BEM VINDO(A) AO CONTROLE FINANCEIRO PESSOAL - by Gleydson Freitas.\n'
          'DEFINA UMA DAS OPÇÕES ABAIXO:')
    menu = Ajustes.valida_int('[1] GERIR COMPRAS - [2] GERIR SALARIO - [3] GERIR RENDIMENTO - [4] GERIR CATEGORIA - [5] ESTATÍSTICAS - [0] FECHAR PROGRAMA: ',
                              'Digite um número inteiro',
                              'Devido as tentativas sem sucesso, o programa será encerrado...', 2)
    match menu:
        case 0:
            bd.desconectar()
            break
        case 1:
            while True:
                Ajustes.limpa_tela(0)
                print('Nesta seção temos as opções para lidar com compras')
                escolha = Ajustes.valida_int('O que você deseja?\n'
                                             '[1] INSERIR COMPRA - [2] - ALTERAR COMPRA - [3] - DELETAR COMPRA - [4] - MENU ANTERIOR: ',
                                             'Digite um valor válido.', 10)
                if escolha == 1:
                    while True:
                        if contador > 0:
                            c = Funcao.continuar(contador, 'inserir nova compra?')
                            if c == 0:
                                contador = 0
                                break
                            else:
                                contador = 0
                        print('Certo, primeiro determine o mês que irá conter a compra: ')
                        Ajustes.apresenta_mes()
                        mes = Funcao.escolher_mes()
                        if mes == 0:
                            break
                        else:
                            print(f'A compra será inserida no mês {meses[mes - 1]}')
                            ver_cat = bd.select_simples('id_cat', 'nome', 'categoria')
                            if len(ver_cat) > 0:
                                print('Escolha a categoria que a compra será inserida!')
                                for dado, tup in enumerate(ver_cat):
                                    if dado % 2 != 0:
                                        verificador += 1
                                        print(f'Código: {verificador} --- {ver_cat[dado]}.')
                                    else:
                                        pass
                                verificador = 0
                            else:
                                print('Você ainda não inseriu categorias, por favor, faça isso para seguir!')
                                Ajustes.limpa_tela()
                                break
                            escolha_cat = Ajustes.valida_int('Digite o código da categoria desejada: ', 'Opção inválida.',
                                                             'Tentativas encerradas, retornando ao menu anterior', 10)
                            if escolha_cat == 0:
                                break
                            elif escolha_cat > (len(ver_cat) / 2):
                                print('Opção não corresponde a nenhuma categoria.')
                                Ajustes.limpa_tela()
                            else:
                                tipo_compra = Ajustes.valida_int('A compra será parcelada[1] ou à vista[2]? ', 'Opção inválida',
                                                                 'Devido as tentativas sem sucesso, a opção retrocedeu', 10)
                                if tipo_compra == 0:
                                    break
                                elif tipo_compra == 1:
                                    limite = bd.select_composto(1, 'categoria', 'limite_gasto', 'id_cat', escolha_cat)
                                    limite_atual = limite[0]
                                    nome = bd.select_composto(1, 'categoria', 'nome', 'id_cat', escolha_cat)
                                    gasto_atual = categorias.somar_gasto_cat(mes, escolha_cat)
                                    if gasto_atual[0] is None:
                                        pass
                                    else:
                                        limite_atual = limite[0] - gasto_atual[0]
                                    valor = Ajustes.valida_float('Digite o valor da compra! R$: ', 'Digite um número real.')
                                    if valor > limite_atual:
                                        print(f'O limite mensal da categoria {nome[0]} é de R${limite[0]}.\n'
                                              f'A compra inserida ultrapassa esse valor...\n'
                                              f'Retornando ao menu inicial de compras.')
                                        Ajustes.limpa_tela()
                                        break
                                    else:
                                        parcela = Ajustes.valida_int('Digite a quantidade de parcelas ', 'Digite um número inteiro', '')
                                        total_valor = valor * parcela
                                        nome_compra = str(input('Digite o nome da compra[Caso não queira por um, apenas dê enter]: '))
                                        compras.adicionar_compra_p(total_valor, parcela)
                                        id_ultimo = bd.select_ultimo('id_compra', 'total_compra')
                                        for compra in range(parcela):
                                            if verificador == 0:
                                                compras.adicionar_valor(valor, mes, escolha_cat, an, nome_compra, id_ultimo[0])
                                                verificador += 1
                                                mes += verificador
                                            else:
                                                if mes <= 12:
                                                    compras.adicionar_valor(valor, mes, escolha_cat, an, nome_compra, id_ultimo[0])
                                                    mes += verificador
                                                else:
                                                    mes, verificador = 1, 1
                                                    an += 1
                                                    compras.adicionar_valor(valor, mes, escolha_cat, an, id_ultimo[0])
                                                    mes += verificador
                                        an = int(ano.year)
                                        verificador = 0
                                        print('Valores inseridos com sucesso!')
                                        Ajustes.limpa_tela()
                                        contador += 1
                                elif tipo_compra == 2:
                                    limite = bd.select_composto(1, 'categoria', 'limite_gasto', 'id_cat', escolha_cat)
                                    limite_atual = limite[0]
                                    nome = bd.select_composto(1, 'categoria', 'nome', 'id_cat', escolha_cat)
                                    gasto_atual = categorias.somar_gasto_cat(mes, escolha_cat)
                                    if gasto_atual[0] is None:
                                        pass
                                    else:
                                        limite_atual = limite[0] - gasto_atual[0]
                                    limite_atual = float(limite_atual)
                                    valor = Ajustes.valida_float('Digite o valor da compra! R$: ', 'Digite um número real.')
                                    if valor > limite_atual:
                                        print(f'O limite mensal da categoria {nome[0]} é de R${limite[0]}.\n'
                                              f'A compra inserida ultrapassa esse valor...\n'
                                              f'Retornando ao menu inicial de compras.')
                                        Ajustes.limpa_tela()
                                        break
                                    else:
                                        nome_compra = str(input('Digite o nome da compra[Caso não queira por um, apenas dê enter]: '))
                                        compras.adicionar_valor(valor, mes, escolha_cat, an, nome_compra)
                                        print('Valor inserido com sucesso!')
                                        Ajustes.limpa_tela()
                                        contador += 1
                elif escolha == 2:
                    while True:
                        if contador > 0:
                            c = Funcao.continuar(contador, 'alterar outra compra?')
                            if c == 0:
                                contador = 0
                                break
                            else:
                                contador = 0
                        else:
                            Ajustes.limpa_tela(0)
                            print('Perfeito, para isso agora defina o mês da compra a ser ajustada')
                            Ajustes.apresenta_mes()
                            mes = Funcao.escolher_mes()
                            if mes == 0:
                                break
                            else:
                                tabela = Funcao.apresentar_compras(bd.conectar(), mes, an, mostrar_id=True)
                                print('Observação: As alterações são feitas apenas dentro do ano vigente. Se precisar mudar mais que isso'
                                      ', por favor, delete a compra e a insira novamente!')
                                if tabela == 0:
                                    Ajustes.limpa_tela(4)
                                    break
                                else:
                                    escolher_alt = Funcao.escolher_compra_edit(bd.conectar(),
                                                                               'Digite o ID que aparece na frente da compra que deseja mudar: ',
                                                                               tabela)
                                    if escolher_alt == 'n':
                                        Ajustes.limpa_tela()
                                        break
                                    else:
                                        novo_valor = Ajustes.valida_float(f'Digite o valor novo para a compra ID({escolher_alt}) R$:', 'Digite um valor válido.')
                                        id_gasto_t = bd.select_composto(1, 'valor', 'compra_total', 'id_valor', escolher_alt)
                                        if id_gasto_t[0] == 1:
                                            compras.alterar_valor(novo_valor, escolher_alt)
                                        else:
                                            parcelas = bd.select_composto(1, 'total_compra', 't_parcela', 'id_compra', id_gasto_t[0])
                                            compras.alterar_valor(novo_valor, escolher_alt, id_gasto_t[0], novo_valor * parcelas[0])
                                            contador += 1
                                            Ajustes.limpa_tela(4)
                elif escolha == 3:
                    while True:
                        if contador > 0:
                            c = Funcao.continuar(contador, 'deletar outra compra?')
                            if c == 0:
                                contador = 0
                                break
                            else:
                                contador = 0
                        else:
                            Ajustes.limpa_tela(0)
                            print('Deletar, né? Vamos definir primeiro o mês da compra.')
                            Ajustes.apresenta_mes()
                            mes = Funcao.escolher_mes()
                            if mes == 0:
                                break
                            else:
                                tabela = Funcao.apresentar_compras(bd.conectar(), mes)
                                print('Lembre-se, para deletar valores de anos futuros ou passados, basta apenas escolher o mês onde o valor se encontra.')
                                if tabela == 0:
                                    Ajustes.limpa_tela(4)
                                    break
                                else:
                                    deleta = Funcao.escolher_compra_edit(bd.conectar(), 'Digite o ID da compra que será deletada: ', tabela)
                                    print(f'A remoção será de todas as parcelas atreladas a compra ID({deleta}). ')
                                    c = Funcao.continuar(1, 'continuar? ')
                                    if deleta == 'n':
                                        Ajustes.limpa_tela()
                                        break
                                    if c == 1:
                                        compras.deletar_valor(deleta)
                                        Ajustes.limpa_tela(4)
                                        contador += 1
                                    else:
                                        print('Retornando ao menu anterior')
                                        Ajustes.limpa_tela()
                                        break
                elif escolha == 4:
                    print('Certo, voltando ao menu anterior.')
                    Ajustes.limpa_tela()
                    break
        case 2:
            while True:
                Ajustes.limpa_tela(0)
                print('Nesta seção trataremos de salários.')
                escolha = Ajustes.valida_int('O que você deseja?\n'
                                             '[1] INSERIR SALÁRIO - [2] - ALTERAR SALÁRIO - [3] - DELETAR SALÁRIO - [4] - MENU ANTERIOR: ',
                                             'Digite um valor válido.', 10)
                if escolha == 1:
                    while True:
                        if contador > 0:
                            c = Funcao.continuar(contador, 'inserir novo salário?')
                            if c == 0:
                                contador = 0
                                break
                            else:
                                contador = 0
                        Ajustes.limpa_tela(0)
                        print('Certo, primeiro determine o mês que irá conter o salário: ')
                        Ajustes.apresenta_mes()
                        mes = Funcao.escolher_mes()
                        if mes == 0:
                            break
                        else:
                            print(f'O salário será inserido no mês {meses[mes - 1]}')
                            inserir_sal = Ajustes.valida_float('Digite o valor do salário: R$', 'Valor inválido.')
                            while True:
                                ano = Ajustes.valida_int('Digite o ano que o salário será incluído: ',
                                                         'Digite um número inteiro', '')
                                if ano < an:
                                    print('Ano inválido, digite um valor maior ou igual ao ano atual.')
                                else:
                                    break
                            salarios.inserir_salario(inserir_sal, mes, ano)
                            Ajustes.limpa_tela()
                            contador += 1
                elif escolha == 2:
                    while True:
                        if contador > 0:
                            c = Funcao.continuar(contador, 'alterar outro salário?')
                            if c == 0:
                                contador = 0
                                break
                            else:
                                contador = 0
                        else:
                            Ajustes.limpa_tela(0)
                            print('Perfeito, para isso agora defina o mês do salário a ser ajustado')
                            Ajustes.apresenta_mes()
                            mes = Funcao.escolher_mes()
                            if mes == 0:
                                break
                            else:
                                tabela = Funcao.apresentar_salarios(bd.conectar(), mes)
                                if tabela == 0:
                                    Ajustes.limpa_tela(4)
                                    break
                                else:
                                    escolher_alt = Funcao.escolher_compra_edit(bd.conectar(),
                                                                               'Digite o ID que aparece na frente do salário que deseja mudar: ',
                                                                               tabela)
                                    if escolher_alt == 'n':
                                        Ajustes.limpa_tela()
                                        break
                                    else:
                                        novo_valor = Ajustes.valida_float(
                                            f'Digite o valor novo para o salário ID({escolher_alt}) R$:',
                                            'Digite um valor válido.')
                                        salarios.alterar_salario(novo_valor, escolher_alt)
                                        contador += 1
                                        Ajustes.limpa_tela(4)
                elif escolha == 3:
                    while True:
                        if contador > 0:
                            c = Funcao.continuar(contador, 'deletar outro salário?')
                            if c == 0:
                                contador = 0
                                break
                            else:
                                contador = 0
                        else:
                            Ajustes.limpa_tela(0)
                            print('Deletar, né? Vamos definir primeiro o mês do salário.')
                            Ajustes.apresenta_mes()
                            mes = Funcao.escolher_mes()
                            if mes == 0:
                                break
                            else:
                                tabela = Funcao.apresentar_salarios(bd.conectar(), mes)
                                print(
                                    'Lembre-se, para deletar valores de anos futuros ou passados, basta apenas escolher o mês onde o valor se encontra.')
                                if tabela == 0:
                                    Ajustes.limpa_tela(4)
                                    break
                                else:
                                    deleta = Funcao.escolher_compra_edit(bd.conectar(),
                                                                         'Digite o ID do salário que será deletado: ', tabela)
                                    print(f'Salário de ID({deleta}) será deletado. ')
                                    c = Funcao.continuar(1, 'continuar? ')
                                    if c == 1:
                                        salarios.deletar_salario(deleta)
                                        Ajustes.limpa_tela(4)
                                        contador += 1
                                    else:
                                        print('Retornando ao menu anterior')
                                        Ajustes.limpa_tela()
                                        break
                else:
                    print('Tudo bem, retornando ao menu anterior.')
                    Ajustes.limpa_tela()
                    break

        case 3:
            while True:
                Ajustes.limpa_tela(0)
                print('Nesta seção trataremos de rendimentos, que nada mais são (aqui) do que ganhos extras que você obtêm!')
                escolha = Ajustes.valida_int('O que você deseja?\n'
                                             '[1] INSERIR RENDIMENTO - [2] - ALTERAR RENDIMENTO - [3] - DELETAR RENDIMENTO - [4] - MENU ANTERIOR: ',
                                             'Digite um valor válido.', 10)
                if escolha == 1:
                    while True:
                        if contador > 0:
                            c = Funcao.continuar(contador, 'inserir novo rendimento?')
                            if c == 0:
                                contador = 0
                                break
                            else:
                                contador = 0
                        Ajustes.limpa_tela(0)
                        print('Certo, primeiro determine o mês que irá conter o rendimento: ')
                        Ajustes.apresenta_mes()
                        mes = Funcao.escolher_mes()
                        if mes == 0:
                            break
                        else:
                            print(f'O rendimento será inserido no mês {meses[mes - 1]}')
                            inserir_red = Ajustes.valida_float('Digite o valor do rendimento: R$', 'Valor inválido.')
                            while True:
                                ano = Ajustes.valida_int('Digite o ano que o rendimento será incluído: ',
                                                         'Digite um número inteiro', '')
                                if ano < an:
                                    print('Ano inválido, digite um valor maior ou igual ao ano atual.')
                                else:
                                    break
                            salarios.inserir_rendimento(inserir_red, mes, ano)
                            Ajustes.limpa_tela()
                            contador += 1
                elif escolha == 2:
                    while True:
                        if contador > 0:
                            c = Funcao.continuar(contador, 'alterar outro rendimento?')
                            if c == 0:
                                contador = 0
                                break
                            else:
                                contador = 0
                        else:
                            Ajustes.limpa_tela(0)
                            print('Perfeito, para isso agora defina o mês do rendimento a ser ajustado')
                            Ajustes.apresenta_mes()
                            mes = Funcao.escolher_mes()
                            if mes == 0:
                                break
                            else:
                                tabela = Funcao.apresentar_rendimentos(bd.conectar(), mes)
                                if tabela == 0:
                                    Ajustes.limpa_tela(4)
                                    break
                                else:
                                    escolher_alt = Funcao.escolher_compra_edit(bd.conectar(),
                                                                               'Digite o ID que aparece na frente do rendimento que deseja mudar: ',
                                                                               tabela)
                                    if escolher_alt == 'n':
                                        Ajustes.limpa_tela()
                                        break
                                    else:
                                        novo_valor = Ajustes.valida_float(
                                            f'Digite o valor novo para o rendimento ID({escolher_alt}) R$:',
                                            'Digite um valor válido.')
                                        salarios.alterar_salario(novo_valor, escolher_alt)
                                        contador += 1
                                        Ajustes.limpa_tela(4)
                elif escolha == 3:
                    while True:
                        if contador > 0:
                            c = Funcao.continuar(contador, 'deletar outro rendimento?')
                            if c == 0:
                                contador = 0
                                break
                            else:
                                contador = 0
                        else:
                            Ajustes.limpa_tela(0)
                            print('Deletar, né? Vamos definir primeiro o mês do rendimento.')
                            Ajustes.apresenta_mes()
                            mes = Funcao.escolher_mes()
                            if mes == 0:
                                break
                            else:
                                tabela = Funcao.apresentar_rendimentos(bd.conectar(), mes)
                                print(
                                    'Lembre-se, para deletar valores de anos futuros ou passados, basta apenas escolher o mês onde o valor se encontra.')
                                if tabela == 0:
                                    Ajustes.limpa_tela(4)
                                    break
                                else:
                                    deleta = Funcao.escolher_compra_edit(bd.conectar(),
                                                                         'Digite o ID do rendimento que será deletado: ',
                                                                         tabela)
                                    print(f'Rendimento de ID({deleta}) será deletado. ')
                                    c = Funcao.continuar(1, 'continuar? ')
                                    if c == 1:
                                        salarios.deletar_rendimento(deleta)
                                        Ajustes.limpa_tela(4)
                                        contador += 1
                                    else:
                                        print('Retornando ao menu anterior')
                                        Ajustes.limpa_tela()
                                        break
                else:
                    print('Tudo bem, retornando ao menu anterior.')
                    Ajustes.limpa_tela()
                    break
        case 4:
            while True:
                Ajustes.limpa_tela(0)
                print(
                    'Nesta seção trataremos de categorias, elas servem para ajuda-lo(a) a administrar suas compras, inserindo limites e afins!')
                escolha = Ajustes.valida_int('O que você deseja?\n'
                                             '[1] CRIAR CATEGORIA - [2] - ALTERAR CATEGORIA - [3] - ORIENTAÇÕES DE USO - [4] - MENU ANTERIOR: ',
                                             'Digite um valor válido.', 10)
                if escolha == 1:
                    while True:
                        if contador > 0:
                            c = Funcao.continuar(contador, 'inserir nova categoria?')
                            if c == 0:
                                contador = 0
                                break
                            else:
                                contador = 0
                        Ajustes.limpa_tela(0)
                        inserir_cat = str(input('Digite o nome da categoria: '))
                        limite_min = Ajustes.valida_float(f'Qual será o limite mínimo para a categoria {inserir_cat} [0] para nenhum. R$:',
                                                          'Digite um número real')
                        limite_max = Ajustes.valida_float(f'Certo, agora qual o limite máximo da {inserir_cat}? R$:',
                                                          'Digite um número real')
                        categorias.inserir_categoria(inserir_cat, limite_max, limite_min)
                        Ajustes.limpa_tela(4)
                        contador += 1
                elif escolha == 2:
                    while True:
                        if contador > 0:
                            c = Funcao.continuar(contador, 'alterar outra categoria?')
                            if c == 0:
                                contador = 0
                                break
                            else:
                                contador = 0
                        else:
                            Ajustes.limpa_tela(0)
                            tabela = Funcao.apresentar_categorias(bd.conectar())
                            if tabela == 0:
                                Ajustes.limpa_tela(4)
                                break
                            else:
                                escolher_alt = Funcao.escolher_compra_edit(bd.conectar(),
                                                                           'Digite o ID que aparece na frente do rendimento que deseja mudar: ',
                                                                           tabela)
                                if escolher_alt == 'n':
                                    Ajustes.limpa_tela()
                                    break
                                else:
                                    nome_cat = bd.select_composto(1, 'categoria', 'nome', 'id_cat', escolher_alt)
                                    escolha_mudanca = Ajustes.valida_int('O que deseja mudar? [1] - Nome - [2] - Gasto mínimo - [3] - Limite - [4] - Outros cenários: ', 'Digite um número válido', '')
                                    match escolha_mudanca:
                                        case 1:
                                            novo_nome = str(input(f'Digite o novo nome para a categoria {nome_cat[0]}: '))
                                            categorias.alterar_categoria(escolher_alt, novo_nome)
                                            Ajustes.limpa_tela()
                                        case 2:
                                            novo_min = Ajustes.valida_float(f'Digite o gasto mínimo para a categoria {nome_cat[0]}. R$:', 'Digite um número real.')
                                            categorias.alterar_categoria(escolher_alt, minimo=novo_min)
                                            Ajustes.limpa_tela()
                                        case 3:
                                            novo_max = Ajustes.valida_float(f'Digite o novo limite para a categoria {nome_cat[0]}. R$:', 'Digite um número real.')
                                            categorias.alterar_categoria(escolher_alt, limite=novo_max)
                                            Ajustes.limpa_tela()
                                        case 4:
                                            novas_ops = Ajustes.valida_int('[1] - Nome e limite - [2] Limite e mínimo - [3] - Nome e mínimo - [4] - Tudo: ',
                                                                           'Digite um número válido', '')
                                            match novas_ops:
                                                case 1:
                                                    novo_nome = str(input(f'Digite o novo nome para a categoria {nome_cat[0]}: '))
                                                    novo_max = Ajustes.valida_float(
                                                        f'Digite o novo limite para a categoria {nome_cat[0]}. R$:',
                                                        'Digite um número real.')
                                                    categorias.alterar_categoria(escolher_alt, novo_nome, novo_max)
                                                    Ajustes.limpa_tela()
                                                case 2:
                                                    novo_max = Ajustes.valida_float(
                                                        f'Digite o novo limite para a categoria {nome_cat[0]}. R$:',
                                                        'Digite um número real.')
                                                    novo_min = Ajustes.valida_float(
                                                        f'Digite o gasto mínimo para a categoria {nome_cat[0]}. R$:',
                                                        'Digite um número real.')
                                                    categorias.alterar_categoria(escolher_alt, limite=novo_max, minimo=novo_min)
                                                    Ajustes.limpa_tela()
                                                case 3:
                                                    novo_nome = str(input(f'Digite o novo nome para a categoria {nome_cat[0]}: '))
                                                    novo_min = Ajustes.valida_float(
                                                        f'Digite o gasto mínimo para a categoria {nome_cat[0]}. R$:',
                                                        'Digite um número real.')
                                                    categorias.alterar_categoria(escolher_alt, novo_nome, minimo=novo_min)
                                                    Ajustes.limpa_tela()
                                                case 4:
                                                    novo_nome = str(input(f'Digite o novo nome para a categoria {nome_cat[0]}: '))
                                                    novo_max = Ajustes.valida_float(
                                                        f'Digite o novo limite para a categoria {nome_cat[0]}. R$:',
                                                        'Digite um número real.')
                                                    novo_min = Ajustes.valida_float(
                                                        f'Digite o gasto mínimo para a categoria {nome_cat[0]}. R$:',
                                                        'Digite um número real.')
                                                    categorias.alterar_categoria(escolher_alt, novo_nome, novo_max, novo_min)
                                                    Ajustes.limpa_tela()
                                                case _:
                                                    print('Opção inválida.')
                                                    Ajustes.limpa_tela()
                                        case _:
                                            print('Opção inválida.')
                                            Ajustes.limpa_tela()
                                    contador += 1
                elif escolha == 3:
                    Ajustes.limpa_tela(0)
                    print('Gostaria de deixar algumas instruções que facilitarão seu uso das categorias.\n'
                          '>Não é possível deletar uma categoria, se precisar de uma nova, sugiro alterar uma já existente na opção 2 do menu anterior.\n'
                          '>Sempre preze pelos limites da categoria, colocandos de maneira real ao seus ganhos mensais.\n'
                          '>Caso tenha inserido uma compra em uma categoria errada, basta deletar a compra no menu respectivo.\n'
                          '>Maiores dúvidas você poderá conferir na FAQ, disposta no menu principal.\n'
                          '...Em 30 segundos você retornará ao menu de categorias =)')
                    Ajustes.limpa_tela(30)
                else:
                    print('Tudo bem, retornando ao menu anterior.')
                    Ajustes.limpa_tela()
                    break
        case 5:
            print('a')