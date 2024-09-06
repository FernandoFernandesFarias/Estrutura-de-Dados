import numpy as np

class VetorOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultimaPosicao = -1
    self.valores = np.empty(self.capacidade, dtype=str)

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
    if self.ultimaPosicao == -1:
      print('Vetor vazio')
    else: 
      for i in range(self.ultimaPosicao + 1):
        print(f'Posição {i} | Valor {self.valores[i]}')

  def pesquisaBinaria(self, valor):
    limiteInferior = 0
    limiteSuperior = self.ultimaPosicao

    while limiteInferior <= limiteSuperior:
      posicaoAtual = (limiteInferior + limiteSuperior) // 2

      print(f'Limite superior {limiteSuperior} | Limite inferior {limiteInferior}')
      if self.valores[posicaoAtual] == valor:
        return posicaoAtual
        
      elif self.valores[posicaoAtual] < valor:
        limiteInferior = posicaoAtual + 1
      else:
        limiteSuperior = posicaoAtual - 1

    return -1
  
  def pesquisar(self, valor):
    for i in range(self.ultimaPosicao + 1):
      if self.valores[i] == valor:
        return i
    return -1

  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      print("Valor não encontrado para exclusão")
      return
    else:
      for i in range(posicao, self.ultimaPosicao):
        self.valores[i] = self.valores[i + 1]
      self.ultimaPosicao -= 1

meuVetor = VetorOrdenado(8)
meuVetor.inserir("F")
meuVetor.inserir("E")
meuVetor.inserir("R")
meuVetor.inserir("N")
meuVetor.inserir("A")
meuVetor.inserir("N")
meuVetor.inserir("D")
meuVetor.inserir("O")
meuVetor.imprimir()
print(meuVetor.pesquisaBinaria('F'))
print(meuVetor.pesquisaBinaria('A'))
print(meuVetor.pesquisaBinaria('O'))

meuVetor.excluir('F')
meuVetor.excluir('A')
meuVetor.excluir('D')
meuVetor.imprimir()
