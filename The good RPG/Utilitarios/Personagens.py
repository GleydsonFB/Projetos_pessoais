from time import sleep


class ator:
    def __init__(self, nome, hp, atk, defe, defe_magica):
        self.nome = nome
        self.hp = hp
        self.atk = atk
        self.defe = defe
        self.defm = defe_magica

    def mostrar_status(self):
        print(f'\tPersonagem: {self.nome}')
        sleep(1.5)
        print(f'\tAtaque: {self.atk}')
        sleep(1.5)
        print(f'\tDefesa física: {self.defe}')
        sleep(1.5)
        print(f'\tDefesa mágica: {self.defm}')
        sleep(1.5)

class npc:
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


