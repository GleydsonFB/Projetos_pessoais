from random import randint
from time import sleep


class Batalha:
    def __init__(self, ator, v_hp, v_nome, v_atk, v_defe, v_defm, v_soco, v_chute):
        self.hp = ator.hp
        self.nome = ator.nome
        self.atk = ator.atk
        self.df = ator.defe
        self.dm = ator.defm
        self.soco = ator.soco
        self.chute = ator.chute
        self.hp2 = v_hp
        self.nome2 = v_nome
        self.atk2 = v_atk
        self.df2 = v_defe
        self.dm2 = v_defm
        self.soco2 = v_soco
        self.chute2 = v_chute

    def luta(self):
        turnos = 1
        inicializa = 0
        contador = 0
        while True:
            if inicializa == 0:
                print('Combate inicializado!')
                inicializa += 1
            else:
                print(f'Turno {turnos}.')
                turnos += 1
                acao = randint(1, 2)
                print(acao)
                dano_j = [self.soco - self.df2, self.chute - self.df2]
                dano_v = [self.soco2 - self.df, self.chute2 - self.df]
                if acao == 1:
                    print(f'{self.nome2} te ataca com um soco, ',
                          f'causando {dano_v[0]} de dano!' if dano_v[0] > 0 else
                          'sendo completamente bloqueado por você')
                    sleep(2)
                    if dano_v[0] > 0:
                        self.hp -= dano_v[0]
                else:
                    print(f'{self.nome2} te ataca com um chute, ',
                          f'causando {dano_v[1]} de dano!' if dano_v[1] > 0 else
                          'sendo completamente bloqueado por você')
                    sleep(2)
                    if dano_v[1] > 0:
                        self.hp -= dano_v[1]
                print('Sua vez, o que irá fazer?')
                jogada = int(input('1 - para atacar com soco ou 2 - para chute: '))
                while jogada not in (1, 2):
                    jogada = int(input('Opção inválida, 1 para soco ou 2 para chute: '))
                    contador += 1
                    if contador == 3:
                        break
                if jogada == 1:
                    print(f'Você ataca {self.nome2} com um soco, ',
                          f'causando {dano_j[0]} de dano!' if dano_j[0] > 0 else
                          f'sendo completamente bloqueado por {self.nome2}.')
                    sleep(2)
                    if dano_j[0] > 0:
                        self.hp2 -= dano_j[0]
                elif jogada == 2:
                    print(f'Você ataca {self.nome2} com um chute, ',
                          f'causando {dano_j[1]} de dano!' if dano_j[1] > 0 else
                          f'sendo completamente bloqueado por {self.nome2}.')
                    sleep(2)
                    if dano_j[1] > 0:
                        self.hp2 -= dano_j[1]
                elif contador == 3:
                    print(f'Você perdeu a vez de atacar =/')
            if self.hp <= 0 or self.hp2 <= 0:
                break
        print('Fim de combate')
        if self.hp <= 0 and self.hp2 > 0:
            print('Você perdeu a luta :(')
            return 2
        elif self.hp2 <= 0 and self.hp > 0:
            print('Você conseguiu a vitória!')
            return 1
        elif self.hp <= 0 and self.hp2 <= 0:
            if self.hp < self.hp2:
                print('Apesar da luta ter sido intensa, você não conseguiu a vitória...')
                return 2
            elif self.hp2 < self.hp:
                print('Mesmo com toda a dificuldade, a vitória é sua!')
                return 1
            else:
                sorteio = randint(1, 2)
                if sorteio == 1:
                    print(f'Com suas últimas forças, você finalizou {self.nome2}!')
                    return 1
                else:
                    print(f'Com o poder que restava, {self.nome2} te derrotou...')
                    return 2