from math import sqrt


def masodik():
    n = int(input("szám: "))
    prim = True
    i = 2.0
    if n < 2:
        prim = False
    else:
        while(i <= sqrt(n)) and (n % i != 0):
            i += 1
        if i > sqrt(n):
            prim = True
        else:
            prim = False
    print(sqrt(n))
    print(i)
    print("Prím? - ", end="")
    if prim:
        print("Prím")
    else:
        print("Nem prím")
