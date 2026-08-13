"""
Öznitelik mühendisliği 

Amaç : 
  1. Mevcut sütunlardan yeni öznitelik üretmen mantığını basit bir örnek ile uygulama
  2. Korelasyon üzerinde modele daha faydalı olabilecek öznitelikleri seçme mantığını gösterme

Adımlar:
  1. Veri setini yükleme
  2. Mevcut üstunlardan yeni öznitelikler üretmek
  3. Hedef değişken ile öznitelikler arasındaki korelasyonlar inceleme
  5. Mutlak korelasyon değerine göre yüksek olan özniteliklerin seçilmesi

"""
import pandas as pd
df = pd.read_csv("oznitelik_muhendisligi_pratik.csv")
print(df)

  
# 2. Mevcut üstunlardan yeni öznitelikler üretmek
df["deneyim_orani"] = df["deneyim_yili"] / df["yas"]
df["yillik_harcama_tahmini"] = df["aylik_harcama"] * 12
print(df.head())

# 3. Hedef değişken ile öznitelikler arasındaki korelasyonlar inceleme

sayisal_df = df.drop("sehir",axis=1)
korelasyonlar = sayisal_df.corr(numeric_only=True)["performans_puani"].sort_values(ascending=False)
print(korelasyonlar)


"""
performans_puani          1.000000
deneyim_orani             0.821244
deneyim_yili              0.597232
yillik_harcama_tahmini    0.317301
aylik_harcama             0.317301
yas                      -0.224902
uyelik_suresi_ay         -0.238212

"""

#  5. Mutlak korelasyon değerine göre yüksek olan özniteliklerin seçilmesi

secilen_oznitelikler = korelasyonlar[abs(korelasyonlar) > 0.75].index.to_list()
secilen_oznitelikler.remove("performans_puani")

print(secilen_oznitelikler)