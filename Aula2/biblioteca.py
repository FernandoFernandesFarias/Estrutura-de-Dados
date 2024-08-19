class Livro:
  def __init__(self, titulo, autor, disponivel = True):
    self.titulo = titulo
    self.autor = autor
    self.disponivel = disponivel

class Usuario:
  def __init__(self, nome):
    self.nome = nome
    self.livrosEmprestados = []

  def emprestarLivro(self, livro):
    if livro.disponivel:
      livro.disponivel = False
      self.livrosEmprestados.append(livro)
      print(f'{self.nome} pegou o livro: {livro.titulo}')

  def devolverLivro(self, livro):
    if livro in self.livrosEmprestados:
      livro.disponivel = True
      self.livrosEmprestados.remove(livro)
      print(f'{self.nome} devolveu o livro: {livro.titulo}')

  
class Biblioteca:
  def __init__(self, nome):
    self.nome = nome
    self.livros = []

  def adicionarLivro(self, livro):
    self.livros.append(livro)

  def exibirLivros(self):
     for livro in self.livros:
      print(f'{livro.titulo} por {livro.autor}')

  def emprestarLivro(self, usuario, titulo):
    for livro in self.livros:
      if livro.titulo == titulo:
        usuario.emprestarLivro(livro)
        return
    
  def devolverLivro(self, usuario, titulo):
    for livro in self.livros:
      if livro.titulo == titulo:
        usuario.devolverLivro(livro)
        return
      
  def livrosDisponiveis(self):
    for livro in self.livros:
      if livro.disponivel:
        print(f'{livro.titulo} por {livro.autor}')

livro1 = Livro('Harry Potter', 'Jorge')
livro2 = Livro('Menino Maluquinho', 'Fábio')
livro3 = Livro('Jogos Vorazes', 'Mateus')
livro4 = Livro('A arte da guerra', 'Roberto')

usuario1 = Usuario('Carlos')
usuario2 = Usuario('Luís')

biblioteca = Biblioteca('Bib Center')
biblioteca.adicionarLivro(livro1)
biblioteca.adicionarLivro(livro2)
biblioteca.adicionarLivro(livro3)
biblioteca.adicionarLivro(livro4)

print(f'Livros disponíveis na {biblioteca.nome}')
print('')
biblioteca.exibirLivros()
print('/' * 40)

biblioteca.emprestarLivro(usuario1, livro2.titulo)
biblioteca.emprestarLivro(usuario2, livro4.titulo)
biblioteca.devolverLivro(usuario1, livro2.titulo)
print('/' * 40)
biblioteca.livrosDisponiveis()



  

