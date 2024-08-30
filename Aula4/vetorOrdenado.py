import numpy as np

class vetorOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultimaPosicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)

  def inserir(self, valor):
    if self.ultimaPosicao == self.capacidade - 1:
      print('Vetor cheio')
      return
    
    posicao = 0
    for i in range(self.ultimaPosicao + 1):
      posicao = i
      if self.valores[i] > valor:
        break

      if i == self.ultimaPosicao:
        posicao = i + 1

    j = self.ultimaPosicao
    while j >= posicao:
      self.valores[j + 1] = self.valores[j]
      j -= 1

    self.valores[posicao] = valor
    self.ultimaPosicao += 1

  def imprimir(self):
    if self.ultimaPosicao == - 1:
      print('Vetor vazio')
    else: 
      for i in range(self.ultimaPosicao + 1):
        print(f'Posição {i} | Valor {self.valores[i]}')

  def pesquisaBinaria(self, valor):
    limiteInferior = 0
    limiteSuperior = self.ultimaPosicao

    while True:
      posicaoAtual = (limiteInferior + limiteSuperior) // 2

      print(f'Limite superior {limiteSuperior} | Limite inferior {limiteInferior}')
      if self.valores[posicaoAtual] == valor:
        return posicaoAtual
      
      elif limiteInferior > limiteSuperior:
        return -1
      
      else:

        if self.valores[posicaoAtual] < valor:
          limiteInferior = posicaoAtual + 1
        else:
          limiteSuperior = posicaoAtual - 1
    
  def pesquisar(self, valor):
    for i in range(self.ultimaPosicao - 1):
      if self.valores[i] > valor:
        return -1

      if valor == self.valores[i]:
        return i 
  
  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultimaPosicao):
        self.valores[i] = self.valores[i + 1]
      self.ultimaPosicao -= 1
        

meuVetor = vetorOrdenado(7)
meuVetor.inserir(9)
meuVetor.inserir(4)
meuVetor.inserir(5)
meuVetor.inserir(8)
meuVetor.inserir(2)
meuVetor.inserir(3)
meuVetor.inserir(1)
meuVetor.inserir(12)
meuVetor.imprimir()
meuVetor.pesquisaBinaria(5,)
