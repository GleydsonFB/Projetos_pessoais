from random import randint
from time import sleep
from .Erros import valida_int
from .Drop import Drops
from .Inventario import Inventario
from .UX import limpa_tela, texto_tela


class Batalha:
    def __init__(self, ator, vilao):
        self.hp = ator.hp
        self.nome = ator.nome
        self.atk = ator.atk
        self.df = ator.defe
        self.soco = ator.soco
        self.chute = ator.chute
        self.hp2 = vilao.hp
        self.nome2 = vilao.nome
        self.df2 = vilao.defe
        self.soco2 = vilao.soco
        self.chute2 = vilao.chute
        self.nome_armav = vilao.nome_arma
        self.dano_armav = vilao.dano_arma

    def luta(self, mochila):
        print('Hora de se preparar para o  combate.')
        arma = Inventario.equipar_arma(mochila, self.atk)
        if arma[1] == 0:
            sleep(2)
            print('A falta de uma arma pode ser fatal!')
            sleep(2)
        sleep(2)
        limpa_tela()
        inicializa, jogada, turnos, acoes = 0, 0, 1, 0
        while True:
            if inicializa == 0:
                print('Combate inicializado!')
                sleep(1)
                inicializa += 1
            else:
                sleep(2)
                print(f'Turno {turnos}.')
                sleep(2)
                turnos += 1
                acao = randint(1, 3)
                dano_j = [self.soco - self.df2, self.chute - self.df2, arma[1] - self.df2]
                dano_v = [self.soco2 - self.df, self.chute2 - self.df, self.dano_armav - self.df]
                if acao == 1:
                    print(f'{self.nome2} te ataca com um soco,',
                          f'causando {dano_v[0]} de dano!' if dano_v[0] > 0 else
                          'sendo completamente bloqueado por você.')
                    sleep(2)
                    if dano_v[0] > 0:
                        self.hp -= dano_v[0]
                elif acao == 2:
                    print(f'{self.nome2} te ataca com um chute,',
                          f'causando {dano_v[1]} de dano!' if dano_v[1] > 0 else
                          'sendo completamente bloqueado por você.')
                    sleep(2)
                    if dano_v[1] > 0:
                        self.hp -= dano_v[1]
                else:
                    print(f'{self.nome2} te ataca usando {self.nome_armav},',
                          f'causando {dano_v[2]} de dano!' if dano_v[2] > 0 else
                          'sendo completamente bloqueado por você.')
                    sleep(2)
                    if dano_v[2] > 0:
                        self.hp -= dano_v[2]
                print('Sua vez, o que irá fazer?')
                while jogada <= 0 or jogada > 3:
                    jogada = valida_int('Digite 1 para golpear com um soco, 2 para chute ou 3 para arma: ',
                                        'Opção inválida, 1 soco, 2 chute, 3 arma: ', 3)
                    acoes += 1
                    if acoes == 3:
                        jogada = 0
                        break
                acoes = 0
                if jogada == 1:
                    sleep(1)
                    print(f'Você ataca {self.nome2} com um soco,',
                          f'causando {dano_j[0]} de dano!' if dano_j[0] > 0 else
                          f'sendo completamente bloqueado por {self.nome2}.')
                    jogada = 0
                    sleep(2)
                    if dano_j[0] > 0:
                        self.hp2 -= dano_j[0]
                elif jogada == 2:
                    sleep(1)
                    print(f'Você ataca {self.nome2} com um chute,',
                          f'causando {dano_j[1]} de dano!' if dano_j[1] > 0 else
                          f'sendo completamente bloqueado por {self.nome2}.')
                    sleep(2)
                    jogada = 0
                    if dano_j[1] > 0:
                        self.hp2 -= dano_j[1]
                elif jogada == 3:
                    if arma[1] > 0:
                        sleep(1)
                        print(f'Você ataca {self.nome2} usando {arma[0]},',
                              f'causando {dano_j[2]} de dano!' if dano_j[2] > 0 else
                              f'sendo completamente bloqueado por {self.nome2}.')
                        if dano_j[2] > 0:
                            self.hp2 -= dano_j[2]
                        sleep(3)
                    else:
                        sleep(1)
                        print('Você não possui uma arma')
                        sleep(1)
                        print("Por conta dessa ação, você acabou perdendo a vez --'")
                    jogada = 0
                elif jogada == 0:
                    print(f'Você perdeu a vez de atacar =/')
                    sleep(2)
                if self.hp <= 0 or self.hp2 <= 0:
                    limpa_tela()
                    break
                else:
                    print(f'{self.nome2} ainda tem {self.hp2} de vida.')
                    print(f'Já você, mantém {self.hp} ponto(s) de vida!')
                    sleep(3.5)
                    limpa_tela()
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


def final_luta(resultado, loot, mochila, nome_vilao):
    """
    :param mochila: Recebe o objeto de inventário do personagem;
    :param resultado: Receberá o valor do resultado (1 para vitória ou 2 para derrota);
    :param loot: Recebe o drop do monstro, em caso de vitória;
    :param nome_vilao: Recebe o nome do oponente;
    :return: Retorna o resultado bem como a opção de inserir o drop no inventário.
    """
    item = Drops(loot[0], loot[1])
    contador = 0
    if resultado == 1:
        print(f'De {nome_vilao} você obteve {item.nome_item}!')
        escolha = str(input('Deseja adicionar este item ao seu inventário? '))
        while escolha not in 'SsNn':
            escolha = str(input('Digite S ou N: '))
            contador += 1
            if contador == 5:
                break
        if contador == 5:
            print(f'Devido ao tempo perdido, o item {item.nome_item} acabou ficando inapto para uso.')
        elif escolha in 'SsNn':
            if escolha in 'Nn':
                print(f'Por sua opção, você perdeu o item {item.nome_item}.')
            else:
                sleep(2)
                n_item = item.caiu(nome_vilao)
                sleep(2)
                Inventario.adicionar(mochila, n_item[0]+' - Dano: '+str(n_item[2]), n_item[1])
