x = 10
if x > 5:
    print("x ist größer als 5")

for i in range(10):
    if i == 5:
        print("Schleife bei 5 unterbrochen")
        break
    print(i)

count = 0
while count < 5:
    if count == 2:
        pass  # Platzhalter, tut nichts
    print(f"Count: {count}")
    count += 1

try:
    zahl = int(input("Gib eine Zahl ein: "))
    print(f"Die eingegebene Zahl ist: {zahl}")
except ValueError:
    print("Das war keine gültige Zahl!")