def calc_divisores(n, d):
    if (d == 0):
        return 0

    if (n % d == 0):
        return 1 + calc_divisores(n, d - 1)

    else:
        return calc_divisores(n, d - 1)


def qtd_divisores(n):
    return calc_divisores(n, n)

n = int(input())
print("Quantidade de divisores de {:d}: {:d}".format(n, qtd_divisores(n)))
