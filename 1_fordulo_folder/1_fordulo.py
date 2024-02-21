"""
# 1. feladat: relatív prímek
# a feladat
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

# b feladat megoldas
counter = 0

num2 = 2354211341
with open("C:/Users/theki/Documents/Python/1_fordulo_folder/szamok.txt", "r") as f:
	print("file opened")
	numbers = f.readlines()
	numbers = [int(i.strip()) for i in numbers]

	print(numbers)
	for i in numbers:
		if sorted(str(i)) == sorted(str(num2)):
			counter += 1
print("A fájlban tárolt számok között", counter, "olyan szerepel, amelynek a számjegyei megegyeznek a 2354211341 számjegyeivel.")
