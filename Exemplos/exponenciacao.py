def exponenciacao(numero, expoente):
    if (expoente == 0):
        return 1

    return numero * exponenciacao(numero, expoente - 1)

numero, expoente = map(int, input().split())
print(exponenciacao(numero, expoente))