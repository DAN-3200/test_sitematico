import subprocess, time, Modulo

def LimparTela(tempo):
    time.sleep(tempo)
    subprocess.run('cls', shell = True)

Category = Modulo.Categoria
Product = Modulo.Produto

# -------------
# Onde vai ser guardado as informações
boxClass = []
boxProd = []

LimparTela(0.3)
debounce = True
while debounce:
  try:
    LimparTela(0)
    print(
        "--------------- Menu ----------------",
        "1 - Cadastrar Categoria",
        "2 - Excluir Categoria",
        "3 - Cadastrar Produto",
        "4 - Excluir Produto",
        "5 - Exibir Produtos Cadastrados",
        "6 - Adicionar Estoque ao Produto",
        "7 - Remover Estoque de Produto",
        "8 - Sair", sep='\n'
    )
  
    Target = str(input("Digite: "))
  
    if Target == '1':
      # Cadastrar Categoria
      LimparTela(0)
      
      print("Categoria ----")
      Nome = str(input("  Nome: "))
      Percentual = int(input("  Percentual: "))
      Category.inserir(boxClass, Category(Nome, Percentual))
      
    elif Target == '2':
      # Excluir Categoria
      LimparTela(0)
      
      print("Excluir Categoria ----")
      Nome = str(input("  Nome: "))
      Category.excluir(boxClass, Nome)
      
    elif Target == '3':
      # Cadastrar Produto
      LimparTela(0)
      
      print("Produto ----")
      Nome = str(input("  Nome: "))
      Custo = int(input("  Preço: "))
      for i,v in enumerate(boxClass):
        print(f"  {i} - {v}")
      index = int(input("  Escolha a categoria: "))
      
      Product.inserir(boxProd, Product(Nome, Custo, boxClass[index]))
  
    elif Target == '4':
      # Excluir Produto
      
      LimparTela(0)
      print("Excluir Produto ----")
      Nome = str(input("  Nome: "))
      Product.excluir(boxProd, Nome)
  
    elif Target == '5':
      # Exibir Produtos
      LimparTela(0)

      print("Exibir Produtos ----")

      # Printar os Produtos
      for i in boxProd:
        print(i)
     
      print("\n","# Espere por 20s")
      time.sleep(20)
        
    elif Target == '6':
      # Editar o estoque do Produto
      LimparTela(0)
      
      print("Estoque ----")
       # Printar os Produtos
      for i, v in enumerate(boxProd):
        print(f"{i} -- {v.nome}")

      index = int(input("  Editar: "))
      try:
        boxProd[index].estoque = int(input("  Estoque: "))
      except:
        # caso não exista ainda o produto
        print("Não há correspondente")
        time.sleep(2)
        
    elif Target == '7':
      LimparTela(0)
      
      # Retirar do Estoque
      print("Remover Estoque ----")
      for i, v in enumerate(boxProd):
        print(f"{i} -- {v.nome}")

      index = int(input("  Editar: "))
      try:
        retirada = int(input("  Retirada: "))
        if (boxProd[index].estoque - retirada) >= 0:
            boxProd[index].estoque -= retirada
        else:
          print("O Valor do estoque não pode ir abaixo de 0")
          time.sleep(2.5)
          
      except:
        print("Não há correspondente")
        time.sleep(2)
    
    elif Target == '8':
      LimparTela(0)
      debounce = False
    
    elif Target == '/acess':
      # caso queira ver o 'banco' durante a aplicação
      LimparTela(0)

      for i in range(20):
        print("Class: ", boxClass)
        print("Produtos: ", boxProd)
        print(f"{i + 1}")
        LimparTela(1)

    else:
      print("Não há algo correspondete")
      LimparTela(0.5)
      
  except:
    LimparTela(0)
    # Não pode deixar o codigo 'cair'
    print("Houve um erro no código, portanto retornaremos ao Menu")
    time.sleep(2.5)
    
else:
    # Caso queira ver tudo no final
    print("Class: ", boxClass)
    print("Produtos: ", boxProd)



