ad = "Kaan"
yas = 25
ortalama = 3.45

print(type(ad))
print(type(yas))
print(type(ortalama))



yas1 = int(input("Yaşın Kaç ?"))
print(type(yas1))
print(yas1 + 5)


urunfiyat = 22.45
kdv = urunfiyat * 0.18 + urunfiyat
print(round(kdv,2)) 


sayilar = [10,20,30,40,50]
print(sayilar[0])
print(sayilar[4])
print(sayilar[2:])
sayilar.append(60)
sayilar.remove(20)
print(sayilar)


koordinat = (12,34)
x,y = koordinat

print(f"{x} \n {y}")
# koordinat[0] = 99

ogrenci = {
  "isim": "Ayse",
  "yas": 22,
  "bolum": "yazılım"
}

print(ogrenci["isim"])
ogrenci["not"] = 90
ogrenci["yas"] = 23
print(ogrenci)

liste = ["ali","ayse","ali","mehmet","ayse"]
benzersiz = set(liste)
print(benzersiz)
print(len(benzersiz))