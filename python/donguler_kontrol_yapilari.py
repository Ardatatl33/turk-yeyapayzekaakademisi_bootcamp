sayi = int(input(f"Bir sayı girin \n"))
if sayi > 0 :
  print("Sayı pozitif")
elif sayi == 0:
  print("Sayi 0")
else:
  print("Sayi negatif")



toplam = 0
for i in range(1,11):
  toplam += i
  print(i)
print(toplam)


giris = ""
while giris != "q" :
  giris = input(f"bir harf girin \n")
  if giris != "q":
    print(harf)
print("q girildi çıkış yapıldı") 