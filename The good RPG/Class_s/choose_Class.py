class Classes:
    def __init__(self, escolha):
        self.prof_M = ['Arqueiro', 'Mago', 'Sacerdote', 'Guerreiro']
        self.prof_F = ['Arqueira', 'Maga', 'Sacerdotiza', 'Guerreira']
        self.escolha = escolha
        self.gener = ['M', 'F']
    def profissão(self):
        values_Class = []
        for v in range(len(self.prof_M)):
            values_Class.append(v)
        self.gener = str(input('Olá aventureiro(a), qual será o gênero do seu personagem na jornada? [M] ou [F]: '))
        while self.gener not in 'MmFf':
            self.gener = str(input('Valor inválido, digite M para masculino ou F para feminino: '))
        if self.gener in 'Ff':
            Classes = self.prof_F[self.escolha]
            return Classes

