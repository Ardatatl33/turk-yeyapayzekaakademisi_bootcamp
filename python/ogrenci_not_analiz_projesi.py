import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class OgrenciNotAnalizi:

  def __init__(self,dosyayolu):
    self.dosyayolu = dosyayolu
    self.df = None

  def veriokuma(self):
    try:
      self.df = pd.read_csv(self.dosyayolu)
      if self.df.empty:
        raise ValueError("csv dosyasi bos")

      gerekli_sutunlar = {"isim", "yas", "bolum", "not"}
      if not gerekli_sutunlar.issubset(self.df.columns): 
        raise ValueError(
          f"csv dosyasında gerekli sutunlar eksik" 
          f"Gerekli Sutunlar : {gerekli_sutunlar}"
        )
      self.df["not"] = pd.to_numeric(self.df["not"],errors="raise")

      print("Veri Başarıyla Okundu")
      print(self.df)
    except FileNotFoundError:
      print(f"hata {self.dosyayolu} bulunamadı")
    except pd.errors.EmptyDataError:
      print("csv dosyası bos")
    except ValueError as error :
      print(f"hata : {error}")
    except Exception as e:
      print(f"Beklenmeyen Hata : {e}")

  def numpy_ile_hesaplama(self):
    try:
      if self.df is None:
        raise ValueError("Önce Veri Yüklenmeli")

      notlar = self.df["not"].to_numpy()
      print(f"Ortalama : {np.mean(notlar)}")
      print(f"Standart Sapma : {np.std(notlar)}")
      print(f"Maksimum Not : {np.max(notlar)}")
      print(f"Minimum Not : {np.min(notlar)}")
    except ValueError as hata:
      print(f"Hata: {hata}")
    except Exception as e:
      print(f"Beklenmeyen bir hata oluştu : {e}")

  def filtreleme(self):
    try:
      if self.df is None:
        raise ValueError("Önce Veri Okunmalıdır")

      yuksek_not = self.df[self.df["not"] > 80]
      print(f"Notu 80 den yuksek olanlar : {yuksek_not}")
      yapay_zeka = self.df[self.df["bolum"] == "Yapay Zeka"]
      print(f"Bolumu Yapay Zeka Olanlar : {yapay_zeka}")
      yas = self.df[self.df["yas"] > 22]
      print(f"Yası 22 den buyuk olanlar : {yas}")

    except ValueError as hata:
      print(f"Hata : {hata}")
    except Exception as e:
      print(f"Beklenmedik hata oluştu : {e}")

  def grafik_ciz(self):
    try:
      if self.df is None:
        raise ValueError("Önce Veri Okunmalıdır")

      plt.figure(figsize=(10,5))

      plt.bar(self.df["isim"],self.df["not"])
      plt.title("Ogrenci Not Grafigi")
      plt.xlabel("İsimler")
      plt.ylabel("Notlar")

      plt.tight_layout()

      plt.show()

    except Exception as e :
      print(f"Beklenmedik bir hata oluştu {e}")

  def tum_analizi_calistir(self):

          
          self.veriokuma()

          
          if self.df is None:
              print("analiz durduruldu")
              return
          
        
          self.numpy_ile_hesaplama()

          
          self.filtreleme()

          
          self.grafik_ciz()


if __name__ == "__main__":
    
    dosya_yolu = "C:\\Users\\ahmet\\Desktop\\bootcamp\\python\\ogrenci_notlari.csv"
    sistem = OgrenciNotAnalizi(dosya_yolu)

    sistem.tum_analizi_calistir()

  
    