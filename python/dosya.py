with open("python\\notlar.txt", "w",encoding="utf-8") as dosya:
  dosya.write("50 \n")
  dosya.write("60 \n")
  dosya.write("70 \n")
  dosya.write("80 \n")
  dosya.write("90 \n")


notlar = []

with open("python\\notlar.txt", "r",encoding="utf-8") as dosya:
    for satir in dosya:
      notlar.append(int(satir.strip()))

ortalama = sum(notlar) / len(notlar)
maks = max(notlar)
minim = min(notlar)

print(notlar)
print(ortalama)
print(maks)
print(minim)

if ortalama >= 50:
  with open("python\\sonuc.txt", "w",encoding="utf-8") as dosya:   
    dosya.write("Sınıf Geçti")
    print("Sınıf Geçti")
else:
  with open("python\\sonuc.txt", "w",encoding="utf-8") as dosya: 
    dosya.write("Sınıf Kaldı")  
    print("sınıf kaldı")