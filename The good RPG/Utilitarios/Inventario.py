from .Erros import remove_inv

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
            print(f'Item {item} adicionado com sucesso na slot {verificador + 1} da mochila!')
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

    def espaco_ocupado(self):
        contagem = 0
        for espaco in range(self.tamanho):
            if self.bag[espaco] in 'Vazio':
                pass
            else:
                contagem += 1
        return contagem

    def venda_item(self, posicao, recebido):
        self.bag[posicao] = 'Vazio'
        print('Item vendido com sucesso!')
        self.gold += recebido
