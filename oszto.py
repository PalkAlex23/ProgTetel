from math import sqrt


def osztok(szam):
    lista = []
    index = 2
    while index <= int(sqrt(szam)):
        if szam % index == 0:
            lista.append(index)
        index += 1
    return lista


# print(osztok(10007))


def osztokB():
    prim = False
    n = 9999
    while not prim:
        n += 1
        i = 2
        while i <= sqrt(n) and n % i != 0:
            i += 1
        if i > sqrt(n):
            prim = True
    print(n)
