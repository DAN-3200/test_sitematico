import time

class Categoria:
    """
        self._nome - Nome da Categoria
        self._percentual - Percentual da Categoria
        self._FK  'Foreign Key' : quantos relacionamentos a categoria tem 
    """
  
    def __init__(self, nome, percentual):
        self._nome = nome
        self._percentual = percentual
        self._FK = 0
   
    
    def __str__(self):
        return self._nome.upper()

    # Mudar o termo do endereço do objeto pelo seu self._nome
    def __repr__(self):
        return self._nome.upper()

    @staticmethod
    def inserir(box, key):
        try:
            if len(box) < 5: # Máximo de Cadastro
                box.append(key)
            else:
                print('Chegou ao limite máximo')
                time.sleep(2)
        except:
            print('erro ao inserir')
            time.sleep(2)


    @staticmethod
    def excluir(box, key):
      # Try pra evitar o caos
        try:
          for i in box:
            if key.upper() == i.__str__(): # verificação se há tal na lista
              if i._FK == 0:
                box.remove(i)
              else:
                print("Já existe algo relacionado a está categoria")
                time.sleep(2)
            else:
                print("Não há essa key no Grupo")
                time.sleep(2)
          
        except:
            print('erro ao excluir')
            time.sleep(2)



    @property
    def percentual(self):
        return self._percentual

    @percentual.setter
    def percentual(self, new):
        self._percentual = new

# ----------------------------------------------------------------------------

class Produto:
    """
    Esta Classe servirá de Molde para construção dos objetos Produtos
    nela contem os atributos básico e métodos que ajudaram na gestão das 'List' referentes ao mesmo
    
    """

    def __init__(self, nome, custo, categoria):
        self._nome = nome
        self._custo = custo
        self._estoque = 0
        self._categoria = categoria
        categoria._FK += 1

    def preco_venda(self):
        return self._custo * (1 + (self._categoria._percentual / 100))

    def __str__(self) -> str:
        return f'Produto {self._nome}, categoria {self._categoria}, {self._estoque} em estoque, preço de venda R${self.preco_venda()}'

    # Mudar o termo do endereço do objeto pelo seu self._nome
    def __repr__(self):
        return self._nome.upper()

    @staticmethod
    def inserir(box, key):
        try:
            box.append(key)
        except:
            print('erro ao inserir')


    @staticmethod
    def excluir(box, key):
        try:
          for i in box:
            if key.lower() == i.nome.lower():
                  box.remove(i)
                  i.categoria._FK -= 1
        except:
            print('erro ao excluir')
            time.sleep(2)


    """
      Get e Set de cada Atributo
      ...exceto do nome que só tem o GET
    """

    @property
    def nome(self):
        return self._nome

    # ----------------
    @property
    def custo(self):
        return self._custo

    @custo.setter
    def custo(self, new):
        self._custo = new

    # ----------------
    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, new):
        self._estoque = new

    # ----------------
    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, new):
        self._categoria = new

