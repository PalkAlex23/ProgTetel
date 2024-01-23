import Szek

szekek = []

def beolvas():
    beFajl = open("szekek.txt", "r", encoding="utf-8")
    beFajl.readline()
    adatok = beFajl.readlines()
    for index in range(0, len(adatok)):
        letisztitott = adatok[index].strip()
        darabolt = letisztitott.split("@")
        szek = Szek.Szek(darabolt[0], darabolt[1])
        szekek.append(szek)
        print(szek)
    beFajl.close()
