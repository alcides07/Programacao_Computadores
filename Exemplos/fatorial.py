def fatorial(n):
    if (n == 0):
        return 1
    
    return n * fatorial(n - 1)

n = int(input())
print("Fatorial de {:d} é {:d}".format(n , fatorial(n)))
