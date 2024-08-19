class Tarefa: 
  def __init__(self, descricao, dataLimite, concluida = False):
    self.descricao = descricao
    self.dataLimite = dataLimite

  def marcarComoConcluida(self, tarefa):
    if tarefa.concluida != True:
      tarefa.concluida = True
      print('Tarefa concluída')

  def alterarDataLimite(self, tarefa):
    pass

class Projeto:
  def __init__(self, nome):
    self.nome = nome
    self.tarefas = []

  def adicionarTarefa(self, tarefa):
    self.tarefas.append(tarefa)
    print(f'{tarefa.descricao} - Tarefa adicionada')

  def removerTarefa(self, tarefa):
    self.tarefas.remove(tarefa)
    print(f'{tarefa.descricao} Tarefa excluída')

  def exibirTarefas(self):
    for tarefa in self.tarefas:
      print(f'{tarefa.descricao}, {tarefa.dataLimite}, {tarefa.concluida}')

class Usuario:
  def __init__(self, nome):
    self.nome = nome
    self.projetos = []

  def criarProjeto(self, nome):
    self.nome = nome
    self.projetos.append(nome)
    print(f'{nome} Criou o projeto: {projeto.nome}')

  def removerProjeto(self, projeto):
    self.projetos.remove(projeto)
    print('Tarefa excluída')

  def exibirProjeto(self):
     for projeto in self.projetos:
      print(f'{projeto.descricao}, {projeto.dataLimite}, {projeto.concluida}')

usuario1 = Usuario('Carlos')
tarefa1 = Tarefa('Lavar o carro', '20/08')
projeto = Projeto('Lista de Agosto')

usuario1.criarProjeto('Lista de Agosto')
projeto.adicionarTarefa(tarefa1)
