import matplotlib.pyplot as plt


aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"]
satislar = [120, 150, 170, 160, 200, 220]
karlar = [20, 35, 40, 30, 50, 60]
reklam = [5, 8, 10, 7, 12, 15]

plt.plot(aylar,satislar)
plt.title("Aylara Göre Satıslar")
plt.xlabel("Aylar")
plt.ylabel("Satıslar")
plt.show()

plt.plot(aylar,karlar, color="red")
plt.title("Aylara Göre Karlar")
plt.xlabel("Aylar")
plt.ylabel("Karlar")
plt.show()

plt.plot(aylar,satislar,marker="o")
plt.title("Aylara Göre Satıslar")
plt.xlabel("Aylar")
plt.ylabel("Satıslar")
plt.show()

plt.bar(aylar,satislar)
plt.title("Aylara Göre Satıslar")
plt.xlabel("Aylar")
plt.ylabel("Satıslar")
plt.show()


print("SORU 5")
plt.bar(aylar, reklam, color="green")
plt.title("Aylara Göre Reklam Harcaması")
plt.xlabel("Aylar")
plt.ylabel("Reklam")
plt.show()

plt.pie(satislar,labels=aylar,autopct="%1.1f%%")
plt.title("Satısların Aylara Göre Dagılımı")
plt.axis("equal")
plt.show()

plt.scatter(reklam, satislar)
plt.title("Reklam ve Satış İlişkisi")
plt.xlabel("Reklam Harcaması")
plt.ylabel("Satışlar")
plt.show()

plt.scatter(reklam, karlar, color="red", s=100)
plt.title("Reklam ve Kar İlişkisi")
plt.xlabel("Reklam Harcaması")
plt.ylabel("Kar")
plt.show()

print("SORU 9")
plt.subplot(1, 2, 1)
plt.plot(aylar, satislar, marker="o")
plt.title("Satışlar")

plt.subplot(1, 2, 2)
plt.bar(aylar, karlar, color="orange")
plt.title("Karlar")

plt.show()

print("SORU 10")
plt.subplot(2, 2, 1)
plt.plot(aylar, satislar, marker="o")
plt.title("Satışlar")

plt.subplot(2, 2, 2)
plt.bar(aylar, karlar, color="green")
plt.title("Karlar")

plt.subplot(2, 2, 3)
plt.scatter(reklam, satislar, color="red")
plt.title("Reklam-Satış")

plt.subplot(2, 2, 4)
plt.pie(satislar, labels=aylar, autopct="%1.1f%%")
plt.title("Satış Dağılımı")

plt.tight_layout()
plt.show()



