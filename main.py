from estoque import Estoque
from sistema import Sistema
from produto import ProdutoFisico, ProdutoDigital

estoque = Estoque()

p1 = ProdutoFisico("Teclado", 10)
p2 = ProdutoDigital("Curso Python", 50)

estoque.adicionar(p1)
estoque.adicionar(p2)

sistema = Sistema(estoque)

estoque.listar()
