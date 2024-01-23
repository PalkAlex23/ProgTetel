class Szek:
    def __init__(self, szin, labszam):
        self.szin = szin
        self.labszam = int(labszam)

    def __str__(self):
        return f"Szék színe: {self.szin}, lábak száma: {self.labszam}"
