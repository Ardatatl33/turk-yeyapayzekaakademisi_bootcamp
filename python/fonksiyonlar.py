def ortalama(vize,final):
  return vize * 0.4 + final * 0.6

def harfnotu(sonuc):
    
    if 85 <= sonuc <= 100:
        print("Harf Notu AA")
    elif 75 <= sonuc < 85:
        print("Harf Notu BA")
    elif 65 <= sonuc < 75:
        print("Harf Notu BB")
    elif 55 <= sonuc < 65: 
        print("Harf Notu CB")
    elif 50 <= sonuc < 55:
        print("Harf Notu CC")
    elif 40 <= sonuc < 50:
        print("Harf Notu DD")
    elif 0 <= sonuc < 40:
        print("Harf Notu FF")
    else:
        print("Sonuç Geçersiz")

vize = int(input("vize notunuzu giriniz ? \n"))
final = int(input("final notunuzu giriniz ? \n"))
hesaplanan_ortalama = ortalama(vize, final)
print("Ortalamanız:", hesaplanan_ortalama)
harfnotu(hesaplanan_ortalama)