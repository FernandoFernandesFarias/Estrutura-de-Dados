class vetorNaoOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultimaPosicao = -1
    self.valores = [''] * capacidade

  def inserir(self, valor):
    if self.ultimaPosicao == self.capacidade - 1:
      print('Vetor cheio')
    else:
      self.ultimaPosicao += 1
      self.valores[self.ultimaPosicao] = valor

  def imprimir(self):
    if self.ultimaPosicao == - 1:
      print('Vetor vazio')
    else: 
      for i in range(self.ultimaPosicao + 1):
        print(f'Posição {i} | Valor {self.valores[i]}')

  def pesquisar(self, valor):
    for i in range(self.ultimaPosicao + 1):
      if self.valores[i] == valor:
        return i
    return -1    
  
  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultimaPosicao):
        self.valores[i] = self.valores[i + 1]
      self.ultimaPosicao -= 1
        

meuVetor = vetorNaoOrdenado(4)
meuVetor.inserir(2)
meuVetor.inserir(6)
meuVetor.inserir(23)
meuVetor.inserir(90)
meuVetor.imprimir()
print(meuVetor.pesquisar(23))
meuVetor.excluir(2)
meuVetor.imprimir()