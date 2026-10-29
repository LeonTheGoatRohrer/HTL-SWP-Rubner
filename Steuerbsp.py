import random

def JahreseinkommenBerechnen(steuerzahler_anzahl):
    einkommensListe = []
    for _ in range(steuerzahler_anzahl):
        einkommen = random.randint(5000, 100000)
        einkommensListe.append(einkommen)
    return einkommensListe


def berechnungSteuer(einkommensListe):
    steuerSätze = [0.4, 0.55, 0.75, 0.82]
    steuerKlassenZaehler = {
        "Geringverdiener": 0,
        "Mittelverdiener": 0,
        "Oberschicht": 0,
        "Top1Percent": 0
    }

    for einkommen in einkommensListe:
        if einkommen <= 10000:
            steuerKlassenZaehler["Geringverdiener"] += 1
        elif einkommen <= 30000:
            steuerKlassenZaehler["Mittelverdiener"] += 1
        elif einkommen <= 70000:
            steuerKlassenZaehler["Oberschicht"] += 1
        else:
            steuerKlassenZaehler["Top1Percent"] += 1

    return steuerKlassenZaehler

def Statistics(ergebnis):
    total = sum(ergebnis.values())
    for klasse, anzahl in ergebnis.items():
        prozent = (anzahl / total) * 100 if total > 0 else 0
        print(f"{klasse}: {anzahl} ({prozent:.2f}%)")


if __name__ == "__main__":
    einkommensListe = JahreseinkommenBerechnen(178)
    ergebnis = berechnungSteuer(einkommensListe)

    print("Einkommen:", einkommensListe)
    print("Steuerklassen:", ergebnis)
    Statistics(ergebnis)
