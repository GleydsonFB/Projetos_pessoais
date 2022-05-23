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



