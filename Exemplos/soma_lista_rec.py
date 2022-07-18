def soma_lista(lista):
    tamanho = len(lista)
    if (tamanho == 0):
        return 0

    else:
        sublista = lista.copy()
        sublista.pop()
        return lista[tamanho - 1] + soma_lista(sublista) 

lista = [1, 2, 3, 4, 5]
print("A soma de todos os elementos da lista é: {:d}".format(soma_lista(lista)))