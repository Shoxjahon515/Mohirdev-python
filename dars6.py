# 06-dars. List  
# Sana : 07.08.2025
# Muallif: Shoxjahon Tuymurodov

radius = 10
ism = "Shoxjahon"

mevalar = ['olma', 'anor', 'uzum', 'anjir', 'shaftoli']
narhlar = [12000, 15000, 20000, 25000, 30000]
sonlar = ["bir", "ikki", 3, 4, 5]
ismlar = []

print(mevalar[0])
print(mevalar[-1])
print(mevalar[0].upper())
print(mevalar[0].title())
print(narhlar[0])
print(narhlar[0] + narhlar[1])

hayvonlar = ['tovuq', "tovuq", 'sigir', 'qo\'y', 'echki', 'ot']
hayvonlar.remove('tovuq')
print(hayvonlar)

bozorlik = ['yog\'on', 'kartoshka', 'sabzi', 'piyoz', 'pomidor']
mahsulot = bozorlik.pop(0)
print("men bozordan " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)

mahsulot2 = bozorlik.pop()
print(mahsulot2)

narhlar.remove(12000)
print(narhlar)

ismlar = ['Shoxjahon', 'Muslim', 'Kamron', 'Shoxruxhon', 'Aziz']
print("Assalomu aleykum va rahmatulloh" + " " + ismlar[1] + " ertaga juma. Juma ayyomlaring bilan!" + 
"\n" + ismlar[1] + ", " + ismlar[2] + ", " + ismlar[3] + " ertaga jumaga chiqamiz?" + "\n" +
ismlar[4] + " akamni ham chaqirish kerak! \n" + "Birga ovqatlanamiz!")

sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
print(sonlar)

sonlar[0] = sonlar[0]+sonlar[-1]
sonlar[1] = -67.8
sonlar[4] = sonlar[4] + 37
del sonlar[5]
print(sonlar)

t_shaxslar = ['Amir Temur','Imom Buxoriy', 'ALisher Navoiy']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Muhammadali Eshonqulov']

print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
suhbat qilishni istar edim.\n")

friends = []
friends.append('Muslim')
friends.append('Kamron')
friends.append('Davron')
print(friends)

friends.remove('Muslim')
friends.remove('Kamron')
print(friends)

friends.append('Firdavs')
friends.insert(0, 'Mirziyodulla')
friends.insert(2, 'Jovohir')
print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("Kelgan mehmonlar: ", mehmonlar)