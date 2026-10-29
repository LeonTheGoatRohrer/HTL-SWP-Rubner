# 1. LIST COMPREHENSION – mit if-else

# Aufgabe: Für Zahlen von 0 bis 9 soll eine Liste erstellt werden,
# die "gerade" oder "ungerade" enthält – je nach Zahl.

parity = ["gerade" if i % 2 == 0 else "ungerade" for i in range(10)]
print(parity)



# 2. SET COMPREHENSION – mit einfachem if
# Aufgabe: Erstelle eine Menge aller Quadratzahlen von 0–20,
# aber nur für Zahlen, die durch 3 teilbar sind.

squares = {x * x for x in range(21) if x % 3 == 0}
print(squares)

# 3. DICTIONARY COMPREHENSION – ohne Bedingung
# Aufgabe: Erstelle ein Dictionary mit Zahlen 1–5 als Keys
# und deren Quadraten als Values.

squares_dict = {x: x * x for x in range(1, 6)}
print(squares_dict)
