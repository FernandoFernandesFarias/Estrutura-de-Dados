dicionario = {}

def caracteres():
    string = input('Digite algo: ')
    string = list(string)

    for caracter in string:
        dicionario[caracter] = string.count(caracter)

    print(dicionario)

caracteres()