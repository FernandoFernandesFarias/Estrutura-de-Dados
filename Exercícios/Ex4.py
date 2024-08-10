numeros = []

def adicionaNum():
    for i in range(5):
        numeros.append(int(input(f"Digite o número {i + 1}: ")))
    print(numeros)

adicionaNum()