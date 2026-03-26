class Knoten:
    def __init__(self, wert):
        self.daten = wert
        self.naechster = None

class Liste:
    def __init__(self):
        self.anfang = None

    def hinzufuegen(self, wert):
        neuer_knoten = Knoten(wert)
        # Wenn die Liste leer ist, ist das der erste Knoten
        if self.anfang == None:
            self.anfang = neuer_knoten
        else:
            # Bis zum Ende laufen
            aktuell = self.anfang
            while aktuell.naechster != None:
                aktuell = aktuell.naechster
            # Am Ende anhängen
            aktuell.naechster = neuer_knoten

    def ausgeben(self):
        aktuell = self.anfang
        while aktuell != None:
            print(aktuell.daten)
            aktuell = aktuell.naechster

# Testen
meine_liste = Liste()
meine_liste.hinzufuegen("Hallo")
meine_liste.hinzufuegen("Welt")
meine_liste.ausgeben()