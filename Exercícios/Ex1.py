numeros = []
numerosPar = []

for i in range(5):
  numeros.append(int(input(f"Digite o número {i + 1}: ")))

for numPar in numeros:
  if numPar % 2 == 0:
    numerosPar.append(numPar)

print(numeros)
print(f'Números pares {numerosPar}')