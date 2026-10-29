from Abteilung import Abteilung
from Mitarbeiter import Mitarbeiter

class Firma(Abteilung):
    def __init__(self, Firmenname, Abteilungen: list, Abteilungsname, MitarbeiterListe: list, Abteilungsleiter):
        super().__init__(Abteilungsname, MitarbeiterListe, Abteilungsleiter)
        self.Firmenname = Firmenname
        self.Abteilungen = Abteilungen

    def AddAbteilung(self, AbteilungNeu: Abteilung):
        self.Abteilungen.append(AbteilungNeu)
        print("Abteilung hinzugefügt")

    def RemoveAbteilung(self, AbteilungZuEntfernen: Abteilung):
        if AbteilungZuEntfernen in self.Abteilungen:
            self.Abteilungen.remove(AbteilungZuEntfernen)
            print("Abteilung entfernt")
        else:
            print("Abteilung nicht in Firma gefunden oder existiert nicht")

    def getAnzahlAbteilungen(self):
        return len(self.Abteilungen)
    
    def getAbteilungen(self):
        for i in self.Abteilungen:
            print(f"Abteilung: {i.Abteilungsname} Mitarbeiter: {len(i.MitarbeiterListe)}")
    
    def __str__(self):
        return f"Firma: {self.Firmenname}, Anzahl der Abteilungen: {self.getAnzahlAbteilungen()}, Anzahl Mitarbeiter: {len(self.getAnzahlMitarbeiter)}"
    
    def createFirma(self, Firmenname, Abteilungen: list, Abteilungsname, MitarbeiterListe: list, Abteilungsleiter):
        return Firma(Firmenname, Abteilungen, Abteilungsname, MitarbeiterListe, Abteilungsleiter)
    
# Demo
if __name__ == "__main__":
    Firma1 = Firma("Google", [], "IT", [], None)
    Firma1.AddAbteilung(Abteilung("IT", [], None))
    Firma1.AddAbteilung(Abteilung("HR", [], None))

    Mitarbeiter1 = Mitarbeiter("Sepp", "IT", False, False)
    Mitarbeiter2 = Mitarbeiter("Rolph", "HR", True, True)

    Firma1.Abteilungen[0].AddMitarbeiter(Mitarbeiter1)
    Firma1.Abteilungen[1].AddMitarbeiter(Mitarbeiter2)

    Firma1.getAbteilungen()
    print(Firma1)