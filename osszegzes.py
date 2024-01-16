def elso():
    n = -1
    while n < 0:
        print("N = ", end="")
        n = int(input())
    ossz = 0
    for i in range(1, n+1):
        ossz += i
    print(f"Az első {n} db természetes szám összege: {ossz}")
