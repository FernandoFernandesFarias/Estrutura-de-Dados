class fila:
  def __init__(self, capacidade):
    self.inicio = 0
    self.final = -1
    self.elementos = 0
    self.inicio = 0
    self.capacidade = capacidade
    self.valores = [''] * capacidade

  def filaCheia(self):
    return self.elementos == self.capacidade
  
  def filaVazia(self):
    return self.elementos == 0
  
  def enfileirar(self, valor):
    if self.filaCheia():
      print('Fila cheia!')
      return
    
    if self.final == self.capacidade -1:
      self.final = - 1

    self.final += 1
    self.valores[self.final] = valor
    self.elementos += 1

  def desenfileirar(self):
    if self.filaVazia():
      print('Fila vazia!')
      return
    
    temp = self.valores[self.inicio]
    self.inicio += 1

    if self.inicio == self.capacidade:
      self.inicio = 0

    self.elementos -= 1
    return temp
  
  def primeiro(self):
    if self.filaVazia():
      return -1
    return self.valores[self.inicio]
  
minhaFila = fila(8)

# minhaFila.desenfileirar()

minhaFila.enfileirar('f')
minhaFila.enfileirar('e')
minhaFila.enfileirar('r')
minhaFila.enfileirar('n')
minhaFila.enfileirar('a')
minhaFila.enfileirar('n')
minhaFila.enfileirar('d')
minhaFila.enfileirar('o')

minhaFila.primeiro()

minhaFila.desenfileirar()
minhaFila.desenfileirar()
minhaFila.desenfileirar()

minhaFila.primeiro()
