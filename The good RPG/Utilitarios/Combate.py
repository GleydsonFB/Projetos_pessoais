from random import randint
from time import sleep
from .Erros import valida_int
from .UX import texto_tela


class Batalha:
    def __init__(self, ator, vilao):
        self.hp = ator.hp
        self.nome = ator.nome
        self.atk = ator.atk
        self.df = ator.defe
        self.dm = ator.defm
        self.soco = ator.soco
        self.chute = ator.chute
        self.hp2 = vilao.hp
        self.nome2 = vilao.nome
        self.atk2 = vilao.atk
        self.df2 = vilao.defe
        self.dm2 = vilao.defm
        self.soco2 = vilao.soco
        self.chute2 = vilao.chute

    def luta(self):
        turnos = 1
        inicializa = 0
        while True:
            if inicializa == 0:
                print('Combate inicializado!')
                inicializa += 1
            else:
                sleep(2)
                print(f'Turno {turnos}.')
                sleep(2)
                turnos += 1
                acao = randint(1, 2)
                dano_j = [self.soco - self.df2, self.chute - self.df2]
                dano_v = [self.soco2 - self.df, self.chute2 - self.df]
                if acao == 1:
                    print(f'{self.nome2} te ataca com um soco,',
                          f'causando {dano_v[0]} de dano!' if dano_v[0] > 0 else
                          'sendo completamente bloqueado por você')
                    sleep(2)
                    if dano_v[0] > 0:
                        self.hp -= dano_v[0]
                else:
                    print(f'{self.nome2} te ataca com um chute,',
                          f'causando {dano_v[1]} de dano!' if dano_v[1] > 0 else
                          'sendo completamente bloqueado por você')
                    sleep(2)
                    if dano_v[1] > 0:
                        self.hp -= dano_v[1]
                print('Sua vez, o que irá fazer?')
                jogada = valida_int('Digite 1 para golpear com um soco ou 2 para chute: ',
                                    'Opção inválida, 1 para soco ou 2 para chute: ', 3)
                if jogada == 1:
                    print(f'Você ataca {self.nome2} com um soco,',
                          f'causando {dano_j[0]} de dano!' if dano_j[0] > 0 else
                          f'sendo completamente bloqueado por {self.nome2}.')
                    sleep(2)
                    if dano_j[0] > 0:
                        self.hp2 -= dano_j[0]
                elif jogada == 2:
                    print(f'Você ataca {self.nome2} com um chute,',
                          f'causando {dano_j[1]} de dano!' if dano_j[1] > 0 else
                          f'sendo completamente bloqueado por {self.nome2}.')
                    sleep(2)
                    if dano_j[1] > 0:
                        self.hp2 -= dano_j[1]
                elif jogada == 0:
                    print(f'Você perdeu a vez de atacar =/')
                    sleep(2)
            if self.hp <= 0 or self.hp2 <= 0:
                break
        sleep(2)
        print('Fim do combate!')
        sleep(2)
        if self.hp <= 0 and self.hp2 > 0:
            print('Você perdeu a luta :(')
            sleep(2)
            return 2
        elif self.hp2 <= 0 and self.hp > 0:
            print('Você conseguiu a vitória!')
            sleep(2)
            return 1
        elif self.hp <= 0 and self.hp2 <= 0:
            if self.hp < self.hp2:
                print('Apesar da luta ter sido intensa, você não conseguiu a vitória...')
                sleep(2)
                return 2
            elif self.hp2 < self.hp:
                print('Mesmo com toda a dificuldade, a vitória é sua!')
                sleep(2)
                return 1
            else:
                sorteio = randint(1, 2)
                if sorteio == 1:
                    print(f'Com suas últimas forças, você finalizou {self.nome2}!')
                    sleep(2)
                    return 1
                else:
                    print(f'Com o poder que restava, {self.nome2} te derrotou...')
                    sleep(2)
                    return 2


def final_luta(resultado, drops):
    """
    :param resultado: Receberá o valor do resultado (1 para vitória ou 2 para derrota);
    :param drops: Recebe o drop do monstro, em caso de vitória;
    :return: Retorna o resultado bem como a opção de inserir o drop no inventário.
    """
    