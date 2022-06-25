import random


def qualidade_item():
    normal = [1, 2, 3, 4, 5, 6, 7]
    verde = [8, 9]
    azul = [10]
    escolha = random.randint(1, 10)
    if escolha in normal:
        return 1
    elif escolha in verde:
        return 2
    else:
        return 3


class Drops:
    def __init__(self, nome_item):
        self.nome_item = nome_item
        self.qualidade_item = qualidade_item()

    def caiu(self, inimigo):
        qualidade = self.qualidade_item
        if qualidade == 1:
            qualidade = 'normal'
        elif qualidade == 2:
            qualidade = 'verde'
        else:
            qualidade = 'azul'
        print(f'O item {self.nome_item} caiu do inimigo {inimigo}, a qualidade dele é {qualidade}!\n'
              f'Você também ganhou {self.grana()} moedas de ouro.')
        if qualidade == 'normal':
            return f'{self.nome_item + " normal"}', self.grana()
        elif qualidade == 'verde':
            return f'{self.nome_item + " verde"}', self.grana()
        else:
            return f'{self.nome_item + " azul"}', self.grana()

    def grana(self):
        if self.qualidade_item == 1:
            return random.randint(1, 3)
        elif self.qualidade_item == 2:
            return random.randint(2, 5)
        else:
            return random.randint(4, 8)