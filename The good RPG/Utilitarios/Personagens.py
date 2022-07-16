from time import sleep
from random import randint


class Ator:
    def __init__(self, nome, hp, atk, defe, valor_soco, valor_chute):
        self.nome = nome
        self.hp = hp
        self.atk = atk
        self.defe = defe
        self.soco = valor_soco
        self.chute = valor_chute

    def mostrar_status(self):
        print(f'\tPersonagem: {self.nome}')
        sleep(1.5)
        print(f'\tAtaque: {self.atk}')
        sleep(1.5)
        print(f'\tDefesa física: {self.defe}')
        sleep(1.5)


class Npc:
    def __init__(self, nome, lista_vende, valor_item):
        self.nome = nome
        self.vende = lista_vende
        self.valor = valor_item

    def loja(self, nome_ator):
        print(f'Olá {nome_ator}, em que posso ajudar hoje? Dê uma olhada no que tenho à venda.')
        print(f'{self.nome} te apresenta o que possui na loja: ')
        for item in range(len(self.vende)):
            print(f'{item}° item: {self.vende[item]} custa {self.valor[item]} moedas de ouro')

    def vendas(self, nome_ator, grana):
        print(f'Que ótimo {nome_ator}!\nQual item deseja comprar? ')
        compra = int(input('Digite o número do item desejado [digite -1 se quiser ver os itens novamente]: '))
        if compra == -1:
            for item in range(len(self.vende)):
                print(f'{item}° item: {self.vende[item]} custa {self.valor[item]} moedas de ouro')
            compra = int(input('Qual o item desejado? Digite a posição dele: '))
            while compra not in range(len(self.vende)):
                compra = int(input('Qual o item desejado? Digite a posição dele: '))
            if self.valor[compra] <= grana:
                print(f'O item {self.vende[compra]} foi adquirido! Restaram {grana} moeda(s) de ouro')
                return self.vende[compra]
            else:
                print(f'Você não tem moedas suficientes para comprar este item.')
        else:
            compra = int(input('Qual o item desejado? Digite a posição dele: '))
            while compra not in range(len(self.vende)):
                compra = int(input('Qual o item desejado? Digite a posição dele: '))
            if self.valor[compra] <= grana:
                print(f'O item {self.vende[compra]} foi adquirido! Restaram {grana} moeda(s) de ouro')
                return self.vende[compra]
            else:
                print(f'Você não tem moedas suficientes para comprar este item.')

    def compras(self, nome_ator, inventario):
        print(f'Tudo bem {nome_ator}, me mostre o que você tem.')
        print(f'Você abre o inventário para {self.nome} e espera sua avaliação.')
        inventario.mostrar()
        print(f'Qual item deseja vender, {nome_ator}? ')
        item = int(input('Digite a posição do item: '))
        item -= 1
        while item > (inventario.espaco_ocupado()):
            item = int(input('Digite uma opção válida: '))
        pagamento = randint(1, 3)
        if pagamento > 1:
            print(f'Bem, para este item posso pagar {pagamento} moedas de ouro, você aceita?')
        else:
            print(f'Bem, para este item posso pagar {pagamento} moeda de ouro, você aceita?')
        aceite = int(input('Digite 1 para sim ou 2 para não: '))
        while aceite not in (1, 2):
            aceite = int(input('Digite uma opção válida: '))
        if aceite == 1:
            inventario.venda_item(item, pagamento)
        else:
            print(f'Tudo bem {nome_ator}, passe outro dia, quem sabe este item não me seja mais interessante.')


class Vilao(Ator):
    def __init__(self, nome, hp, atk, defe, valor_soco, valor_chute, nome_arma, dano_arma):
        super().__init__(nome, hp, atk, defe, valor_soco, valor_chute)
        self.nome_arma = nome_arma
        self.dano_arma = dano_arma + atk