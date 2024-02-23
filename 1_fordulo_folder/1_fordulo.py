
# 1. FELADAT: relatív prímek
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

# 2. FELADAT
# A, feladata: populáció
with open("C:/Users/theki/Documents/Python/1_fordulo_folder/telepules.txt", "r") as f:
   village = f.readlines()
   village = [i.strip() for i in village]


population_numbers = [int(i.split()[-4]) for i in village]
min_population_num = min(population_numbers)
print(min_population_num, 'is the minimum population number.')

population_numbers.remove(min_population_num)
new_population_num = min(population_numbers)
print(new_population_num, 'is the second least population number.')
