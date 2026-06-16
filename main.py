from estoque import Estoque
from sistema import Sistema
from produto import ProdutoFisico, ProdutoDigital
from caixa import Caixa

estoque = Estoque()

p1 = ProdutoFisico("Teclado", 10)
p2 = ProdutoDigital("Curso Python", 50)

estoque.adicionar(p1)
estoque.adicionar(p2)

sistema = Sistema(estoque)

print("=== ESTOQUE ===")
estoque.listar()

print("\n=== CAIXA GENÉRICA ===")

caixa = Caixa()

caixa.adicionar(p1)
caixa.adicionar(p2)

for produto in caixa.listar():
    produto.exibir()
