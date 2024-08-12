alunos = {}
continua = ''

while True:
  nome = input('Nome do aluno: ')
  notas = []
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  nota3 = float(input('Nota 3: '))

  notas = [nota1, nota2, nota3]

  alunos[nome] = notas

  continua = input('Deseja continuar? S/N: ')

  if continua == 'N' or continua == 'n':
    break

