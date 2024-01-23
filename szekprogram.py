from Szek import Szek
szekek = []


def masodik():
    print("")
    peldany1 = Szek("kék", 13)
    peldany2 = Szek("piros", 4)
    peldany3 = Szek("zöld", 5)

    print(peldany1)
    print(peldany2)
    print(peldany3)

    szekek.append(peldany1)
    szekek.append(peldany2)
    szekek.append(peldany3)


# összegzés tétel
def labakSzama():
    print("Összesen hány darab szék láb van a teremben? - ", end="")
    ossz = 0
    for index in range(0, len(szekek)):
        ossz += szekek[index].labszam
    print(f"{ossz} db")


# maximum kiválasztás tétel
def maxLabszin():
    maxLab = szekek[0].labszam
    maxSzin = szekek[0].szin
    for index in range(0, len(szekek)):
        if szekek[index].labszam > maxLab:
            maxLab = szekek[index].labszam
            maxSzin = szekek[index].szin
    print(f"A legtöbb lábbal rendelkező szék színe: {maxSzin}")


# megszámlálás tétel
def negynagylab():
    print("Hány négynél több lábú szék van: ", end="")
    db = 0
    for index in range(0, len(szekek)):
        if szekek[index].labszam > 4:
            db += 1
    print(str(db))


# eldöntés tétel
def pirosnegylabu():
    print("Van-e piros négy lábú szék?: ", end="")
    van_e = False
    for index in range(0, len(szekek)):
        if szekek[index].szin == "piros" and szekek[index].labszam == 4:
            van_e = True
    if van_e:
        print("Van")
    else:
        print("Nincs")
