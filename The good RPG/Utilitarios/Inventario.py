class inventario:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.bag = []
        for espaco in range(self.tamanho):
            self.bag.append('Vazio')


    def mostrar(self):
        for espacos in range(self.tamanho):
            tratamento = self.bag[espacos]
            tratamento.replace("'", "")
            tratamento.replace('[', '')
            tratamento.replace(']', '')
            self.bag[espacos] = tratamento
        for visual in range(self.tamanho):
            print(f'{visual +1}° -- {self.bag[visual]}')

    def adicionar(self, item):
        verificador = 0
        adicionado = False
        while verificador < self.tamanho:
            if 'Vazio' not in self.bag[verificador]:
                verificador += 1
            else:
                self.bag[verificador] = item
                adicionado = True
                break
        if adicionado is False:
            print('Bag cheia')
        else:
            print(f'Item {item} adicionado com sucesso na slot {verificador+1}')
