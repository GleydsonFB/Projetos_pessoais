class inventario:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.bag = []
        for espaco in range(self.tamanho):
            self.bag.append(f'{espaco+1}° ------ Vazio')


    def mostrar(self):
        print(self.bag)

    def adicionar(self, item):
        verificador = 0
        while verificador < self.tamanho:
            if 'Vazio' not in self.bag[verificador]:
                verificador += 1
            else:
                self.bag[verificador] = item
                break