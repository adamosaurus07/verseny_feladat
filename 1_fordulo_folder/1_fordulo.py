"""
# 1. feladat: relatív prímek
a,
counter = 0
number = []

with open("C:/Users/theki/Documents/Python/1_fordulo_folder/szamok.txt", "r") as f:
    numbers = f.readlines()

    for i in numbers:
        number.append(int(i))
    from math import gcd as bltin_gcd
    for j in number:
        a = j
        b = 1310438493

        def is_coprime(a, b):
          return bltin_gcd(a, b) == 1
        if is_coprime(a, b):
          counter += 1
print("A fájlban tárolt számok között", counter, "olyan szerepel, amely a 1310438493 számmal relatív prím.")
"""
b,
counter = 0
with open("C:/Users/theki/Documents/Python/1_fordulo_folder/szamok.txt", "r") as f:
    numbers = f.readlines()
    for i in numbers:
        if sorted(str(i)) == sorted(str(2354211341)):
            counter += 1
print("A fájlban tárolt számok között", counter, "olyan szerepel, amely a 2354211341 szám permutációja.")sgsg
