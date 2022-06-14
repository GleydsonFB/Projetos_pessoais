import Utilitarios
from Utilitarios import Inventario
from Utilitarios import Drop
from Utilitarios import Personagens
from Utilitarios import Combate

print('Teste')
jogador = Personagens.Ator('Gleydson', 20, 1, 2, 3, 2, 3)
vilao = Personagens.Ator('Junior', 2, 1, 2, 3, 2, 3)
batalha1 = Combate.Batalha(jogador, vilao.hp, vilao.nome, vilao.atk, vilao.defe, vilao.defm, vilao.soco, vilao.chute)
resultado_batalha1 = batalha1.luta()
print(resultado_batalha1)

