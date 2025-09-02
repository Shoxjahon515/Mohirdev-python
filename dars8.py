# 08-dars. For-loop  
# Sana : 08.08.2025
# Muallif: Shoxjahon Tuymurodov

mehmonlar = ['Ali', 'Muhammad Yusuf', 'Dilshod', 'Mohir']
print("salom", mehmonlar[0])
print("salom", mehmonlar[1])
print("salom", mehmonlar[2])

for mehmon in mehmonlar:
    print("Salom", mehmon)
    print("Hayr", mehmon)
    print("Salom", mehmon)
for mehmonlar in mehmonlar:
    print("Salom", mehmonlar)
    print("Hayr", mehmonlar)

for mehmon1 in mehmonlar:
    print(f"Hurmatli {mehmon1}, sizni 2-oktabrda tug'ilgan kunimga taklif qilaman")
    print(f"Hurmat bilan Shoxjahon")

sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")

sonlar = list(range(11))
print(sonlar)

sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)

print(sonlar)
print(sonlar_kvadrati)

dostlar = []
print("3 ta eng yaqin do'stingiz kim?")
for n in range(3): 
    dostlar.append(input(f"{n+1}-ning do'stingizni ismini kiriting: "))

print(dostlar)

ismlar = []
ism = (input('Ismingizni kiriting:'))
ismlar.append(ism)

for ism in ismlar:
    print(f"Assalom alaykum, {ism}. Python tili juda onson va tez organishingiz mumkin!")


ismlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
for ism in ismlar:
    print(f"Assalom alaykum, {ism}. Sahifamizga xush kelibsiz!")

print(f"Kod {len(ismlar)} marta takrorlandi")

sonlar = list(range(11, 100, 2))
for son in sonlar:
    print(son**3)

kinolar = []
print("5 ta sevimli kinoingiz qaysilar?")
for k in range(5):
    kinolar.append(input(f"{k+1}-kino:"))
print(kinolar)


n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)