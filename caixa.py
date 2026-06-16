from typing import Generic, TypeVar

T = TypeVar("T")

class Caixa(Generic[T]):

    def __init__(self):
        self.__itens: list[T] = []

    def adicionar(self, item: T):
        self.__itens.append(item)

    def listar(self):
        return self.__itens
