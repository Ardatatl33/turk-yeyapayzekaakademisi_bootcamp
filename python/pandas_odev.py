import pandas as pd

veri = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Ahmet", "Elif"],
    "yas": [25, 30, 28, 35, 22, 27],
    "sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "Bursa", "İstanbul"],
    "maas": [5000, 7000, 6000, 8000, 4500, 6500]
}

df = pd.DataFrame(veri)
print(df)

print(df.head(3))

print(df.columns)

print(df["isim"])

print(df[["isim","maas"]])

print(df[df["yas"] > 28])

print(df[df["maas"] > 6000] [["isim","maas"]])

print(df.sort_values("maas"))

print(df.sort_values("maas",ascending = False))

print(df.groupby("sehir")["maas"].sum())

df["yıllık_maas"] = df["maas"] * 12
print(df)