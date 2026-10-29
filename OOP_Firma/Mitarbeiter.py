class Mitarbeiter: 
    def __init__(self, name, abteilung, IsMale: bool, IsAbteilungsleiter: bool):
        self.name = name
        self.abteilung = abteilung
        self.IsMale = IsMale
        self.IsAbteilungsleiter = IsAbteilungsleiter

    def CreateMitarbeiterInfo(self):
        geschlecht = "Männlich" if self.IsMale else "Weiblich"
        rolle = "Abteilungsleiter" if self.IsAbteilungsleiter else "Mitarbeiter"
        return f"{self.name} - {geschlecht}, {rolle} in Abteilung {self.abteilung}"
    
    def __str__(self):
        return self.CreateMitarbeiterInfo()
    
    def createMitarbeiter(self, name, abteilung, IsMale: bool, IsAbteilungsleiter: bool):
        return Mitarbeiter(name, abteilung, IsMale, IsAbteilungsleiter)


