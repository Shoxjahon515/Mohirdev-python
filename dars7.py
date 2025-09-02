# 07-dars. List  
# Sana : 08.08.2025
# Muallif: Shoxjahon Tuymurodov

cars = ['Tesla', 'BMW', 'Mercedes', 'Audi', 'Ford']
cars.sort()
print(cars)

cars2 = ["Tesla", "bmw", "mercedes", "audi", "ford"]
cars2.sort()
print(cars2)

cars = ['Tesla', 'BMW', 'Mercedes', 'Audi', 'Ford']
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
print(sorted(cars, reverse=True))

sonlar = [5, 2, 9, 1, 5, 6]
sonlar.sort()
print(sonlar)
print(sorted(sonlar))
print(sorted(sonlar, reverse=True))
uzunlik = len(sonlar)
print("Uzunligi:", uzunlik)
sonlar = list(range(0,10))
print(sonlar)

toq_sonlar = list(range(1,20,2))
print(toq_sonlar)

juft_sonlar = list(range(0,20,2))
print(juft_sonlar)

sanash = list(range(0,100,10))
print(sanash)


narhlar = [12000, 25000, 125000, 8000,100000]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narh:", arzon, "Eng qimmat narh:", qimmat, "Jami narh:", jami)

cars = ['Tesla', 'BMW', 'Mercedes', 'Audi', 'Ford']
print(cars[0:3])
print(cars[:4])
print(cars[0:])

my_cars = cars
print(cars)
print(my_cars)

my_cars.remove('Audi')
print(my_cars)

my_cars.append("Tesla Y")
print(my_cars)

cars = ["BMW", "Mercedes", "Audi", "Toyota", "Chevrolet", "Tesla"]
# print(cars)

my_cars = cars[:]
cars.remove('Toyota')
print(cars)
print(my_cars)

# Tupple

toys = ('cars', 'teddy', 'snake', 'lizard', 'bear')
print(toys[0])
print(toys[-3])
print(toys[2:5])
print(toys[3:])

toys[0] = "bear2"
toys.append ('makvin')

toys.remove('cars')
print(toys)

toys = list(toys)
print(type(toys))
toys.append('car2')
print(toys)

toys = tuple(toys)
print(type(toys))
print(toys)

davlatlar = ["O'zbekiston", "Qozog'iston", "Rossiya", "Malayziya", "Singapur", "AQSh"]
print(davlatlar)      
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))

davlatlar.reverse
print(davlatlar)

davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

sonlar = list(range(120, 1200, 2))
print(sonlar)
print(sum(sonlar))
print(max(sonlar) - min(sonlar))
print(len(sonlar))
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])

taomlar = ["osh", "somsa", "norin", "shashlik", "qozonkabob"]
nonushta = taomlar[:]

nonushta.remove("norin")
nonushta.remove("shashlik")
nonushta.remove("qozonkabob")
nonushta.append("non va qaymoq")
nonushta.append("issiq non")
print(taomlar)
print(nonushta)

nonushta = tuple(nonushta)
print(nonushta)
nonushta[0] = "qaymoq va non"