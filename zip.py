names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
ages = [23, 17, 34, 15, 20]
scores = [88, 92, 78, 90, 91]

# Liste aus Tupeln (Name, Alter, Score)
x = list(zip(names, ages, scores))

# Filter: nur Personen ab 18
x = list(filter(lambda y: y[1] >= 18, x))

# Filter: Score >= 80
x = list(filter(lambda y: y[2] >= 80, x))

# Umwandlung in ein Dictionary-ähnliches Format
y = list(map(lambda a: {"name": a[0], "age": a[1], "score": a[2]}, x))

print(x)
print(y)
