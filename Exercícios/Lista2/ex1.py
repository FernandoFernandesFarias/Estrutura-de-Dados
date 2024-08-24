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
        

meuVetor = vetorNaoOrdenado(8)
meuVetor.inserir('F')
meuVetor.inserir('E')
meuVetor.inserir('R')
meuVetor.inserir('N')
meuVetor.inserir('A')
meuVetor.inserir('N')
meuVetor.inserir('D')
meuVetor.inserir('O')
meuVetor.imprimir()
print('=' * 30) 
print(meuVetor.pesquisar('R'))
print(meuVetor.pesquisar('F'))
print(meuVetor.pesquisar('O'))
meuVetor.excluir('F')
meuVetor.excluir('A')
meuVetor.excluir('O')
print('=' * 30) 
meuVetor.imprimir()
