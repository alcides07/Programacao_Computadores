def divisores(n, d):
    if (d == 0):
        return 0

    if (n % d == 0):
        print(d)

    return divisores(n, d - 1)

n = int(input())
divisores(n, n)
