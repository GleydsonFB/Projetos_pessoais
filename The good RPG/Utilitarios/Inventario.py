from .Erros import remove_inv, valida_int


class Inventario:
    def __init__(self, tamanho, gold):
        self.tamanho = tamanho
        self.gold = gold
        self.bag = []
        for espaco in range(self.tamanho):
            self.bag.append('Vazio')

    def mostrar(self):
        for espacos in range(self.tamanho):
            tratamento = self.bag[espacos]
            tratamento.replace("'", "")
            tratamento.replace('[', '')
            tratamento.replace(']', '')
            self.bag[espacos] = tratamento
        for visual in range(self.tamanho):
            print(f'{visual + 1}° -- {self.bag[visual]}')
        print(f'Você possui {self.gold} moedas de ouro.')

    def mostrar_gold(self):
        return self.gold

    def adicionar(self, item, gold=0):
        verificador = 0
        adicionado = False
        while verificador < self.tamanho:
            if 'Vazio' not in self.bag[verificador]:
                verificador += 1
            else:
                self.bag[verificador] = item
                adicionado = True
                break
        if adicionado is False:
            print(f'A mochila está cheia!')
        else:
            print(f'Item adicionado com sucesso na slot {verificador + 1} da mochila!')
            if gold > 0:
                print(f'Você recebeu {gold} moeda(s) de ouro!')
                self.gold += gold

    def remover(self):
        verificador = 0
        print('Qual item irá remover?')
        for espacos in range(self.tamanho):
            tratamento = self.bag[espacos]
            tratamento.replace("'", "")
            tratamento.replace('[', '')
            tratamento.replace(']', '')
            self.bag[espacos] = tratamento
        for visual in range(self.tamanho):
            print(f'{visual + 1}° -- {self.bag[visual]}')
        remove = remove_inv('Digite a posição do item escolhido ', 'Posição inválida', self.tamanho)
        remove -= 1
        if self.bag[remove] not in 'Vazio':
            self.bag[remove] = 'Vazio'
            print('Item retirado!')
        else:
            print('O espaço já se encontra vazio')

    def equipar_arma(self):
        """
        Método usado para escolher uma arma do inventário.
        :return: Retorna o nome da arma escolhida.
        """
        self.mostrar()
        while True:
            while True:
                escolha = valida_int('Escolha o slot que possui a arma desejada: ', 'digite um número inteiro')
                if escolha > self.tamanho or escolha <= 0:
                    print('Opção inválida')
                else:
                    escolha -= 1
                    break
            if self.bag[escolha] != 'Vazio' and self.bag[escolha] != 'Poção':
                v = 0
                retorno = []
                retorno_nome = ''
                arma = []
                nome_arma = []
                slot = list(self.bag[escolha])
                for d, p in enumerate(slot):
                    temp = slot[d]
                    temp = str(temp)
                    if temp.isnumeric():
                        retorno.append(temp)
                    else:
                        arma.append(temp)
                while arma[v] != '-':
                    nome_arma.append(arma[v])
                    v += 1
                for espacos in range(v - 1):
                    tratamento = nome_arma[espacos]
                    tratamento.replace("'", "")
                    tratamento.replace('[', '')
                    tratamento.replace(']', '')
                    retorno_nome = retorno_nome+tratamento
                if len(retorno) == 1:
                    return int(retorno[0])
                else:
                    print(f'A arma {retorno_nome} foi equipada com sucesso!')
                    return retorno_nome, int(str(retorno[0])+str(retorno[1]))
            else:
                print('o slot escolhido não contem uma arma!')
