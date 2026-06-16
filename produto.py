from Exibivel import Exibivel

class Produto(Exibivel):

    def __init__(self, nome: str, quantidade: int):
        self.__nome = nome
        self.__quantidade = quantidade

    @property
    def nome(self):
        return self.__nome

    @property
    def quantidade(self):
        return self.__quantidade


class ProdutoFisico(Produto):

    def exibir(self):
        print(f"[FÍSICO] {self.nome} - {self.quantidade}")


class ProdutoDigital(Produto):

    def exibir(self):
        print(f"[DIGITAL] {self.nome} - {self.quantidade}")