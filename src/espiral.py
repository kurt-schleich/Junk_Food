class Espiral:
    def __init__(self):
        self.produto = ' - '
        self.qnt = 0
        self.preco = 0

    def getNomeDoProduto(self):
        return self.produto

    def getQuantidade(self):
        return self.qnt

    def getPreco(self):
        return self.preco

    def setNomeDoProduto(self, nome):
        self.produto = nome

    def setPreco(self, val):
        self.preco = val

    def setQuantidade(self, qnt):
        self.qnt = qnt

    def return_to_zero(self):
        self.produto = ' - '
        self.qnt = 0
        self.preco = 0