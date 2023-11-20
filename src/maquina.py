from Junk_Food.src.espiral import Espiral


class Maquina:

    def __init__(self, qtdEspirais: int, maximoProdutos: int):
        self.espirais = []
        self.cofrinho = 0
        self.inserido = 0
        self.qnt_espiras = qtdEspirais
        self.prod_p_espiras = maximoProdutos
        for i in range(qtdEspirais):
            self.espirais.append(Espiral())

    def getFaturamento(self) -> float:
        return self.cofrinho

    def getMaximoProdutos(self) -> int:
        return self.prod_p_espiras

    def getSaldoCliente(self) -> float:
        return self.inserido

    def getSizeEspirais(self) -> int:
        return self.qnt_espiras

    def getEspiral(self, indice: int) -> Espiral:
        if len(self.espirais) > indice:
            return self.espirais[indice]

    def inserirDinheiro(self, value: float) -> bool:
        if value > 0:
            self.inserido += value
            return True
        else:
            return False

    def receberTroco(self) -> float:
        troco = self.inserido
        self.inserido = 0
        return troco

    def alterarEspiral(self, indice: int, nome: str, quantidade: int, preco: float) -> bool:
        if len(self.espirais) > indice >= 0:
            if self.prod_p_espiras >= quantidade:
                espiral = self.getEspiral(indice)
                espiral.setPreco(preco)
                espiral.setQuantidade(quantidade)
                espiral.setNomeDoProduto(nome)
                return True
            else:
                return False
        else:
            return False

    def limparEspiral(self, indice: int) -> bool:
        if len(self.espirais) > indice > 0:
            espiral = self.getEspiral(indice)
            espiral.return_to_zero()
            return True
        else:
            return False

    def vender(self, indice: int) -> bool:
        if len(self.espirais) > indice > 0:
            espiral = self.getEspiral(indice)
            if espiral.qnt > 0:
                val = espiral.getPreco()
                if self.inserido >= val:
                    espiral.qnt -= 1
                    self.inserido -= val
                    self.cofrinho += val
                    if espiral.qnt == 0:
                        espiral.return_to_zero()
                    return True
            else:
                espiral.return_to_zero()
                return False
        else:
            return False
