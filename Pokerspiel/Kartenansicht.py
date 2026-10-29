from numpy.random import randint

class Karte:
    def __init__(self, farbe, wert, person):
        self.Farbe = farbe
        self.Wert = wert
        self.Person = person

    def anzeigen(self):
        symbole = {
            "Herz": "♥",
            "Karo": "♦",
            "Pik": "♠",
            "Kreuz": "♣"
        }

        # TERNÄRER OPERATOR – genau wie gefordert eingebaut
        symbol = symbole[self.Farbe] if self.Farbe in symbole else "?"

        print("____________")
        print(f"|{self.Person:<2}     {self.Wert:>2} |")
        print("|          |")
        print(f"|     {symbol}    |")
        print("|          |")
        print(f"|__________|")


def randomKarteGenerieren(karte):
    farben = ["Herz", "Karo", "Pik", "Kreuz"]
    karte.Farbe = farben[randint(0, 4)]


def randomNumberGenerieren(karte):
    karte.Wert = randint(1, 11)


def randomKartenPersonGenerieren(karte):
    personen = ["K", "D", "B", "A"]
    karte.Person = personen[randint(0, 4)]


def bewertung(hand):
    werte = sorted([k.Wert for k in hand])
    farben = [k.Farbe for k in hand]

    gleiche_farbe = len(set(farben)) == 1
    werte_counts = {w: werte.count(w) for w in werte}
    straight = sorted(werte) == list(range(min(werte), min(werte) + 5))

    if gleiche_farbe and straight and max(werte) == 14:
        return "Royal Flush"
    if gleiche_farbe and straight:
        return "Straight Flush"
    if 4 in werte_counts.values():
        return "Four of a Kind"
    if sorted(werte_counts.values()) == [2, 3]:
        return "Full House"
    if gleiche_farbe:
        return "Flush"
    if straight:
        return "Straight"
    if 3 in werte_counts.values():
        return "Three of a Kind"
    if list(werte_counts.values()).count(2) == 2:
        return "Two Pair"
    if 2 in werte_counts.values():
        return "One Pair"

    return "High Card"


if __name__ == "__main__":
    for i in range(5):
        karte = Karte("", 0, "")
        randomKarteGenerieren(karte)
        randomNumberGenerieren(karte)
        randomKartenPersonGenerieren(karte)

        print(f"Karte: {karte.Farbe} {karte.Wert} {karte.Person}")
        karte.anzeigen()
        print()
