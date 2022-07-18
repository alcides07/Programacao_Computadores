def calc_divisores(n, d):
    if (d == 1):
        return [1]

    divs = calc_divisores(n, d - 1)

    if (n % d == 0):
        divs.append(d)

    return divs

def divisores(n):
    return calc_divisores(n, n)

n = int(input())
lista_divisores = divisores(n)
print("O número {:d} contém {:d} divisores".format(n, len(lista_divisores)))
print(*lista_divisores, sep = ", ")
