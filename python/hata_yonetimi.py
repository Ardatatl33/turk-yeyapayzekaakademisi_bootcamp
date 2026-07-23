with open("python\\hata.txt","r",encoding="utf-8") as dosya:
  
  veri = []
  for satir in dosya:
    try:
      veri.append(int(satir.strip()))
    except:
      pass
  ortalama = sum(veri) / len(veri)
  print(ortalama)

