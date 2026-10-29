class Schueler:
    def __init__(self, name, alter, klasse):
        self.name = name
        self.alter = alter
        self.klasse = klasse

    def vorstellen(self):
        print("Hallo, ", self.name)
        print("Ich bin", self.alter, "Jahre alt")
        print("Ich geh in die", self.klasse)


schueler1 = Schueler("Franz", 67, "3AHWII")
schueler2 = Schueler("Sepp", 67, "4AHBG")

schueler1.vorstellen()
print("------")
schueler2.vorstellen()
