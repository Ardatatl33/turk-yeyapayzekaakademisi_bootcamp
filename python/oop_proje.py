class sayilar:
  def __init__(self,veriler):
    self.veriler = veriler
  def toplambul(self):
    toplam = sum(self.veriler)
    print(f"Sayilarin Toplamı : {toplam}")
  def ortalama(self):
    ortalama = sum(self.veriler) / len(self.veriler)
    print(f"Sayilarin Ortlaması : {ortalama}")
  def maks(self):
    en_buyuk = max(self.veriler)
    print(f"En Buyuk Sayı : {en_buyuk}")
  def min_sayı(self):
      en_kucuk = min(self.veriler)
      print(f"En Kucuk Sayı : {en_kucuk}")


analiz1 = sayilar([10,20,30,40,50,60,70,80,90,100])
analiz1.toplambul()
analiz1.ortalama()
analiz1.maks()
analiz1.min_sayı()
