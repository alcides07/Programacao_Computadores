def maior2(x, y):
    if (x > y):
        return x
    else:
        return y

def maior_rec(lista):
    tamanho = len(lista)
    if(tamanho == 1):
        return lista[0]

    return maior2(lista[tamanho - 1], maior_rec(lista[:-1]))

lista = [1, 8, 9, 10, 15, 0]
print(maior_rec(lista))