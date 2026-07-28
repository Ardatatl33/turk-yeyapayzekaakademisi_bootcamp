import numpy as np

dizi = np.arange(1,21)
print(dizi)
print(dizi.size)


dizi1 = np.array([5,10,15,20,25])
sonuc = dizi1 * 3
print(sonuc)

dizi2 = np.arange(0,31)
dilim = dizi[10:21]
print(dilim)

dizi3 = np.array(
  [1,2,3]
)
dizi4 = np.array(
  [4,5,6]
)
sonuc1 = np.concatenate((dizi3,dizi4))
print(sonuc1)


dizi = np.arange(1,13)
matris = dizi.reshape(3,4)
print(matris)
print(matris.shape)


matris1 = np.array([
  [1,2,3],
  [4,5,6],
  [7,8,9] 
])

print(matris1[1])
print(matris1[:,1])

matris2 = np.random.rand(3,3)
print(matris2)
print(np.mean(matris2))
print(np.max(matris2))


a = np.array([2,4,6,8])
b = np.array([1,3,5,7])

sonuc = a*b
print(sonuc)


sayilar = np.random.randint(1,51,10)

print(sayilar)
print(np.sum(sayilar))
print(np.mean(sayilar))