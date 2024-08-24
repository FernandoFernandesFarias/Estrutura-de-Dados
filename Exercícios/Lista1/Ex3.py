alunosNotas = {'Jorge': [7, 8, 5], 'Lucas': [3, 10, 8], 'Pedro': [6, 9, 6]}

def alunosMedia(alunosNotas):
  alunoMedia = {}
  for aluno, media in alunosNotas.items():
    medias = sum(media) / len(media)
    alunoMedia[aluno] = medias

  print(alunoMedia)

alunosMedia(alunosNotas)