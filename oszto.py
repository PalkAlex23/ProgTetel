from math import sqrt


def osztok(szam):
    lista = []
    index = 2
    while index <= int(sqrt(szam)):
        if szam % index == 0:
            lista.append(index)
        index += 1
    return lista


print(osztok(10007))
