from produto import Produto

class Estoque:

    def _init_(self):
        self.__produtos = []

    def adicionar(self, produto: Produto):
        self.__produtos.append(produto)

    def listar(self):
        for produto in self.__produtos:
            produto.exibir()
