class Pilha:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.topo = -1
    self.valores = [''] * capacidade
  
  def pilhaCheia(self):
    return self.topo == self.capacidade -1
  
  def pilhaVazia(self):
    return self.topo == -1
  
  def empilhar(self, valor):
    if self.pilhaCheia():
      print('Pilha está cheia')
    else:
      self.topo += 1
      self.valores[self.topo] = valor

  def desempilhar(self):
    if self.pilhaVazia():
      print('Pilha vazia')
    else:
      self.topo -= 1

  def verTopo(self):
    if self.topo != -1:
      return self.valores[self.topo]
    else: return -1

minhaPilha = Pilha(8)

minhaPilha.desempilhar()

minhaPilha.empilhar('F')
minhaPilha.empilhar('e')
minhaPilha.empilhar('r')
minhaPilha.empilhar('n')
minhaPilha.empilhar('a')
minhaPilha.empilhar('n')
minhaPilha.empilhar('d')
minhaPilha.empilhar('o')

minhaPilha.empilhar('F')

minhaPilha.verTopo()

minhaPilha.desempilhar()
minhaPilha.desempilhar()
minhaPilha.desempilhar()

minhaPilha.verTopo()
