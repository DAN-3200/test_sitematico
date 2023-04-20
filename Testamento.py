import unittest
import Modulo

"""
    Este Arquivo tem como propósito testar os Arquivos

    @auto Daniel Barros Moreira
    @date 18/04/2023
"""

# ========== Montagem do cenário ==========

# Pegando as classes
Category = Modulo.Categoria
Product = Modulo.Produto

# Estoque
boxCate = []; boxProd = []


Alimento = Category('Alimento', 10)
Banana = Product('Banana', 5, Alimento)

# ========== Execução/verificação ==========
class test_categoria(unittest.TestCase):
    """
        Aqui será testados os principais métodos de 'Categoria', os quais são:
            - Criar
            - Inserir
            - Excluir
    """

    def test_criar(self):
        # insirindo dados
        Nome = str(input("  Categoria_Nome: "))
        Percentual = int(input("  Categoria_Percentual: "))
        cat_criar = Category(Nome, Percentual)

        self.assertIsInstance(cat_criar, Category)

    def test_inserir(self):
        # insirindo dados
        Nome = str(input("  Categoria_Nome: "))
        Percentual = int(input("  Categoria_Percentual: "))
        cat_inserir = Category(Nome, Percentual)
        Category.inserir(boxCate, cat_inserir)

        self.assertIn(cat_inserir, boxCate)

    def test_excluir(self):
        Nome = str(input("  Categoria_Nome: "))
        Percentual = int(input("  Categoria_Percentual: "))
        cat_excluir = Category(Nome, Percentual)

        Category.inserir(boxCate, cat_excluir)

        Category.excluir(boxCate, cat_excluir.__str__())

        self.assertNotIn(cat_excluir, boxCate)


class test_produto(unittest.TestCase):
    """
          Aqui será testados os principais métodos de 'Produto', os quais são:
              - Criar
              - Inserir
              - Excluir
              - Preco_venda
    """
    def test_criar(self):
        # insirindo dados
        Nome = str(input("  Produto_Nome: "))
        Custo = int(input("  Produto_Custo: "))
        obj = Product(Nome, Custo, Alimento)

        self.assertIsInstance(obj, Product)

    def test_inserir(self):
        # insirindo dados
        Nome = str(input("  Produto_Nome: "))
        Custo = int(input("  Produto_Custo: "))
        obj = Product(Nome, Custo, Alimento)
        Product.inserir(boxProd, obj)

        self.assertIn(obj,boxProd)

    def test_excluir(self):
        Product.inserir(boxProd, Banana)
        Product.excluir(boxProd, Banana.nome)

        self.assertNotIn(Banana, boxProd)

    def test_precoVenda(self):
        self.assertEqual(Banana.preco_venda(), 5.5)

