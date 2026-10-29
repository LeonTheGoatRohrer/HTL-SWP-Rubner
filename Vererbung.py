#einfache 3 stufige Vererbung ein paar mithoder und Oarameter

class Lebewesen:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def info(self):
        return f"{self.name}, {self.alter} Jahre"

class Saeugetier(Lebewesen):
    def __init__(self, name, alter, fellfarbe):
        super().__init__(name, alter)
        self.fellfarbe = fellfarbe
    
    def saeugen(self):
        return f"{self.name} säugt"

class Hund(Saeugetier):
    def __init__(self, name, alter, fellfarbe, rasse):
        super().__init__(name, alter, fellfarbe)
        self.rasse = rasse
    
    def bellen(self):
        return "Wau Wau!"

# Demo
hund = Hund("Bello", 4, "braun", "Retriever")
print(hund.info())
print(hund.bellen())