def maior(lista):
    tamanho = len(lista)
    if(tamanho == 1):
        return lista[0]
    
    print(*lista)
    maior_elemento = maior(lista[:-1])
    print("Maior elemento até agora:", maior_elemento)
    print("{:d} > {:d}".format(lista[tamanho - 1], maior_elemento))
    if (lista[tamanho - 1] > maior_elemento):
        maior_elemento = lista[tamanho - 1]

    return maior_elemento

lista = [1, 8, 9, 10, 15, 0]
print(maior(lista))