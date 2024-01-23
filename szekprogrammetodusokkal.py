from Szek import Szek


# példányosítás
def peldanyok_listaban():
    szekek = []

    peldany1 = Szek("kék", 13)
    peldany2 = Szek("piros", 4)
    peldany3 = Szek("zöld", 5)

    szekek.append(peldany1)
    szekek.append(peldany2)
    szekek.append(peldany3)
    return szekek


# lista kiírás
def listaKiiras(lista: list):
    print("")
    for index in range(0, len(lista)):
        print(lista[index])


# összegzés tétel
def osszegzes(lista):
    print("Összesen hány darab szék láb van a teremben? - ", end="")
    ossz = 0
    for index in range(0, len(lista)):
        ossz += lista[index].labszam
    print(f"{ossz} db")


# maximum kiválasztás tétel
def maximumKivalasztas(lista: list):
    maxLab = lista[0].labszam
    maxSzin = lista[0].szin
    for index in range(0, len(lista)):
        if lista[index].labszam > maxLab:
            maxLab = lista[index].labszam
            maxSzin = lista[index].szin
    print(f"A legtöbb lábbal rendelkező szék színe: {maxSzin}")


# megszámlálás tétel
def megszamlalas(lista: list):
    print("Hány négynél több lábú szék van: ", end="")
    db = 0
    for index in range(0, len(lista)):
        if lista[index].labszam > 4:
            db += 1
    print(str(db))


# eldöntés tétel
def eldontes(lista: list):
    print("Van-e piros négy lábú szék?: ", end="")
    van_e = False
    for index in range(0, len(lista)):
        if lista[index].szin == "piros" and lista[index].labszam == 4:
            van_e = True
    if van_e:
        print("Van")
    else:
        print("Nincs")
