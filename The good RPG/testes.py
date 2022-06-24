from Utilitarios import Combate, Drop, Inventario, Personagens, UX


print('Teste')
bag = Inventario.Inventario(6, 2)
vilao_1 = Personagens.Vilao('Junior', 3, 1, 1, 2, 3, 4)
protagonista = Personagens.Ator('Eu', 10, 1, 2, 3, 2, 3)
batalha_1 = Combate.Batalha(protagonista, vilao_1)
batalha_1.luta()

