from Utilitarios import Combate, Drop, Inventario, Personagens, UX


print('Teste')
item = 'Lança de azura'
bag = Inventario.Inventario(6, 2)
vilao_1 = Personagens.Vilao('Junior', 1, 1, 1, 2, 3, 4)
protagonista = Personagens.Ator('Eu', 10, 1, 2, 3, 2, 3)
batalha_1 = Combate.Batalha(protagonista, vilao_1)
resultado_b1 = batalha_1.luta()
drop_item = Combate.final_luta(resultado_b1, item, vilao_1.nome)
bag.adicionar(drop_item[0], drop_item[1])
bag.mostrar()