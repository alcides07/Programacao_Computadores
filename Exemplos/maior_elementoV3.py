def maior2(x, y):
    if (x > y):
        return x
    else:
        return y

def calc_maior(lista, pos_ultimo):
    if (pos_ultimo == 0):
        return lista[pos_ultimo]
    
    else:   
        return maior2(lista[pos_ultimo], calc_maior(lista, pos_ultimo - 1))

def maior(lista):
    return calc_maior(lista, len(lista) - 1)

lista = [1, 8, 10, 20, 5, 0]
print(maior(lista))