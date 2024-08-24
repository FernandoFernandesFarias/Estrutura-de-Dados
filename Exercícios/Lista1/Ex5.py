numeros = []
i = 0

def somaNum(lista):
    return sum(lista)
    
while i < 5:
    numeros.append(int(input("Digite um número: ")))
    i += 1

print(somaNum(numeros))
