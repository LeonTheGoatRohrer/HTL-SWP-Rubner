from Mitarbeiter import Mitarbeiter

class Abteilung:
    def __init__(self, Abteilungsname, MitarbeiterListe: list, Abteilungsleiter: Mitarbeiter):
        super().__init__()
        self.Abteilungsname = Abteilungsname
        self.MitarbeiterListe = MitarbeiterListe
        self.Abteilungsleiter = Abteilungsleiter

    def AddMitarbeiter(self, mitarbeiter: Mitarbeiter):
        self.MitarbeiterListe.append(mitarbeiter)
        print(f"{mitarbeiter.name} wurde zu {self.Abteilungsname} hinzugefügt")
    
    def getAnzahlMitarbeiter(self):
        return len(self.MitarbeiterListe)
    
    def AddAbteilungsleiter(self, AbteilungsleiterNeu: Mitarbeiter):
        if self.Abteilungsleiter is None:
            self.Abteilungsleiter = AbteilungsleiterNeu
            print("Abteilungsleiter hinzugefügt")
        else:
            #Alten Löschen, neuen Hinzufügen
            self.Abteilungsleiter = AbteilungsleiterNeu
            print("Abteilungsleiter geändert")

    def AddMitarbeiter(self, MitarbeiterNeu: Mitarbeiter):
        self.MitarbeiterListe.append(MitarbeiterNeu)
        print("Mitarbeiter hinzugefügt")

    def RemoveMitarbeiter(self, ZuentferndenderMitArbeiter: Mitarbeiter):
        if ZuentferndenderMitArbeiter in self.MitarbeiterListe:
            self.MitarbeiterListe.remove(ZuentferndenderMitArbeiter)
            print("Mitarbeiter entfernt")
        else:
            print("Mitarbeiter nicht in Abteilung gefunden oder existiert nicht")

    def getAnzahlMitarbeiter(self):
        return len(self.MitarbeiterListe)
    
    def __str__(self):
        return f"Abteilung: {self.Abteilungsname}, Anzahl Mitarbeiter: {self.getAnzahlMitarbeiter()}, Abteilungsleiter: {self.Abteilungsleiter.name if self.Abteilungsleiter else 'Kein Abteilungsleiter'}"
    
    def createAbteilung(self, Abteilungsname, MitarbeiterListe: list, Abteilungsleiter: Mitarbeiter):
        return Abteilung(Abteilungsname, MitarbeiterListe, Abteilungsleiter)
    



    