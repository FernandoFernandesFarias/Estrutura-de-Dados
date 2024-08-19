class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

class Carrinho:
  def __init__(self):
    self.produtos = []
    
  def adicionarProduto(self, produto):
    self.produtos.append(produto)

  def removerProduto(self, produto):
    self.produtos.remove(produto)

  def calcularTotal(self):
    total = 0
    for produto in self.produtos:
      total += produto.preco
    return total

produto1 = Produto('Camiseta', 50)
produto2 = Produto('Calça', 100)
produto3 = Produto('Boné', 30)
produto4 = Produto('Tênis', 200)

carrinho = Carrinho()
carrinho.adicionarProduto(produto1)
carrinho.adicionarProduto(produto2)
carrinho.adicionarProduto(produto3)
carrinho.adicionarProduto(produto4)

print(f'Total da compra: R${carrinho.calcularTotal()}')

