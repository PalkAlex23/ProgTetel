def kicsi():
    VEGE = 0
    db = 0
    mini = 2147483647
    while (szam := int(input("Szám: "))) != VEGE:
        if szam < mini:
            mini = szam
        db += 1
    print(f"{db} számból a legkisebb: {mini}")
