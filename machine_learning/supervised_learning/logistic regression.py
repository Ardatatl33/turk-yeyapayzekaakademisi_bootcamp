"""
Amaç : 
  - UCI Heart Disease veri setini kullanarak logistic regression modeli ile ikili sınıflandırma problemi çözme
  - Model, bir bireyin kalp hastalığına sahip olup olmadığını tahmin etmeyi açılar ve accuracy metriği ile değerlendirilir

Veri seti :
  - UCI Machine learning repo
  - Veri seti bireylere ait demografik ve klinik ölçümlerini içeriyor
  - features : yas cinsiyet ağrı tipi kan basıncı vb.
  - hedef degisken :
      -0 hatsalık yok
      -1 hastalık var
Plan/Porgram:
  1. Veri setini yükle ve temel analizleri yap
  2. Veri seti içerisinde eksik değer kontroli yap gerekirse temizle
  3. Öznitelik ve hedef değişkenleri ayrılması
  4. eğitim ve test veri setlerinin oluşturulması
  5. Logistic regression modelinin tanımlanması ve eğitilmesi
  6. modelin test veri seti ile değerlendirilmesi


"""

from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#   1. Veri setini yükle ve temel analizleri yap

heart_disease = fetch_ucirepo(id = 45)
df = pd.DataFrame(data= heart_disease.data.features)
df["target"] = heart_disease.data.targets
df["target"] = df["target"].apply(lambda x: 0 if x == 0 else 1)

print(df.head())

if df.isna().any().any():
  print(f"nan değerleri veri setinden çıkarttık sayısı: {df.isnull().sum().sum()}")
  df.dropna(inplace=True)
  
else:
  print("nan değer bulunamadı")

# 3. Öznitelik ve hedef değişkenleri ayrılması

X = df.drop(["target"],axis = 1).values
y = df.target.values

#   4. eğitim ve test veri setlerinin oluşturulması

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.1,random_state=42)

#  5. Logistic regression modelinin tanımlanması ve eğitilmesi
log_reg = LogisticRegression(penalty="l2",C = 1, max_iter= 100)
log_reg.fit(X_train,y_train)

# 6. modelin test veri seti ile değerlendirilmesi
acc = log_reg.score(X_test,y_test)
print(f"Accuracy : {acc}")

 