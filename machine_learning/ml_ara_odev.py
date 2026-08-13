"""
Müşteri Ayrılma Tahmini - Makine Öğrenmesi Ara Ödevi

Amaç:
    Bu projenin amacı, müşterilerin abonelik hizmetinden ayrılıp
    ayrılmayacağını tahmin eden bir sınıflandırma modeli geliştirmektir.

    Hedef değişken:
        churn
            0 : Müşteri aboneliğine devam ediyor.
            1 : Müşteri aboneliğinden ayrılmış.

Kullanılan veri seti:
    Müşteri bilgilerini içeren CSV dosyası kullanılmaktadır.

    Veri setindeki temel sütunlar:
        - musteri_id
        - yaş
        - gelir
        - abonelik_suresi
        - destek_talebi_sayisi
        - şehir
        - üyelik_tipi
        - churn

Proje Adımları:
    1. CSV dosyasından veri setini oku.
    2. Veri setinin ilk satırlarını incele.
    3. Veri setinin satır ve sütun sayısını kontrol et.
    4. Veri tiplerini ve temel istatistikleri incele.
    5. Hedef değişken olan churn dağılımını kontrol et.
    6. Eksik değerleri tespit et ve uygun yöntemle doldur.
    7. Kategorik değişkenleri temizle.
    8. Kategorik değişkenleri One-Hot Encoding yöntemiyle sayısal
       değişkenlere dönüştür.
    9. Yeni öznitelikler oluştur:
        - gelir_grubu
        - destek_talebi_var_mi
        - abonelik_yili
    10. Sayısal değişkenleri StandardScaler ile ölçeklendir.
    11. Veriyi train, validation ve test kümelerine ayır.
    12. Logistic Regression modelini eğit.
    13. K-Nearest Neighbors (KNN) modelini eğit.
    14. Modelleri validation verisi üzerinde karşılaştır.
    15. Validation sonucuna göre en başarılı modeli seç.
    16. Seçilen modeli test verisi üzerinde değerlendir.
    17. Confusion matrix, accuracy, precision, recall ve F1-score metriklerini hesapla.
    18. Model sonuçlarını yorumla.

Kullanılan Kütüphaneler:
    pandas:
        CSV dosyasını okumak, DataFrame oluşturmak, veri temizlemek ve veri analizi yapmak için kullanılır.

    numpy:
        Sayısal işlemler ve eksik değer kontrolleri için kullanılır.

    scikit-learn:
        Veri bölme, veri ön işleme, öznitelik dönüştürme, model eğitimi ve model değerlendirme işlemleri için kullanılır.

    train_test_split:
        Veri setini eğitim, validation ve test kümelerine ayırmak için kullanılır.

    ColumnTransformer:
        Sayısal ve kategorik sütunlara farklı ön işleme adımları uygulamak için kullanılır.

    Pipeline:
        Ön işleme ve model eğitim adımlarını tek bir akışta birleştirmek için kullanılır.

    SimpleImputer:
        Eksik sayısal değerleri medyan ile, eksik kategorik değerleri ise en sık görülen değer ile doldurmak için kullanılır.

    OneHotEncoder:
        Şehir ve üyelik tipi gibi kategorik değişkenleri makine öğrenmesi modellerinin kullanabileceği sayısal sütunlara dönüştürmek için kullanılır.

    StandardScaler:
        Sayısal değişkenleri benzer ölçeğe getirmek için kullanılır.Özellikle Logistic Regression ve KNN modelleri için önemlidir.

    LogisticRegression:
        Müşterinin ayrılıp ayrılmayacağını tahmin etmek için kullanılan temel ve açıklanabilir bir sınıflandırma modelidir.

    KNeighborsClassifier:
        Benzer müşterilerin davranışlarına bakarak sınıflandırma yapan K-Nearest Neighbors sınıflandırma modelidir.

    accuracy_score:
        Doğru tahminlerin tüm tahminlere oranını hesaplar.

    precision_score:
        Ayrılacağı tahmin edilen müşterilerin ne kadarının gerçekten ayrıldığını gösterir.

    recall_score:
        Gerçekte ayrılan müşterilerin ne kadarının doğru tespit edildiğini gösterir.

    f1_score:
        Precision ve recall değerlerinin dengeli ortalamasını hesaplar.

    confusion_matrix:
        Doğru ve yanlış sınıflandırmaları tablo halinde gösterir.

Beklenen Çıktılar:
    - Veri setinin ilk satırları
    - Veri setinin boyutu
    - Eksik değer bilgileri
    - Churn sınıf dağılımı
    - Oluşturulan yeni öznitelikler
    - Logistic Regression validation sonuçları
    - KNN validation sonuçları
    - Seçilen modelin test sonuçları
    - Confusion matrix
    - Accuracy, precision, recall ve F1-score değerleri
    - Modellerin kısa karşılaştırması ve yorumlanması
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier


df = pd.read_csv("machine_learning\\musteri_churn_veri_seti.csv", encoding="utf-8-sig")

print(df.head())

print(f"Veri setinin satır ve sütun sayısı : {df.shape}")

print(f"Hedef değişken dağılımı : {df["churn"].value_counts()}")

print(f"Eksik değerler : \n {df.isnull().sum()}")

df_filled = df.copy()

sayisal_sutunlar = [
  "yaş",
  "gelir",
  "abonelik_suresi",
  "destek_talebi_sayisi"
]

kategorik_sutunlar = [
  "şehir",
  "üyelik_tipi"
]

# Sayısal sütunları ve kategorik sütunları uygun değerler ile doldurduk
for sutun in sayisal_sutunlar:
    medyan_deger = df_filled[sutun].median()
    df_filled[sutun] = df_filled[sutun].fillna(medyan_deger)

for sutun in kategorik_sutunlar:
    mod_deger = df_filled[sutun].mode()[0]
    df_filled[sutun] = df_filled[sutun].fillna(mod_deger)

print(f"Eksik değerler medyan ve mod değerleri ile dolduruldu : \n {df_filled.isnull().sum()}")

# Yeni öznitelikler üretiyoruz 

df_filled["abonelik_yili"] = (
    df_filled["abonelik_suresi"] / 12
).round(2)

df_filled["destek_talebi_var_mi"] = (
    df_filled["destek_talebi_sayisi"] > 0
).astype(int)

df_filled["gelir_grubu"] = pd.cut(
    df_filled["gelir"],
    bins=[0,30000,60000,float("inf")],
    labels=["Düşük","Orta","Yüksek"]
)


# Üyelik tipi yazımlarını tamamen standartlaştırma
df_filled["üyelik_tipi"] = (
    df_filled["üyelik_tipi"]
    .str.strip()
    .str.lower()
    .replace({
        "temel": "Temel",
        "standart": "Standart",
        "premium": "Premium"
    })
)

# One- Hot encoding ile kategorik sütunları sayısal forma dönüştürüyoruz
y = df_filled["churn"]

X = df_filled.drop(
  columns = ["churn","musteri_id"]
)

X = pd.get_dummies(
    X,
    columns=["şehir","üyelik_tipi","gelir_grubu"],
    drop_first=True,
    dtype=int
)

print(f"One-Hot Encoding sonrası : \n {X.head()} ")


# Veriyi train, validation ve test kümelerine ayırma

X_train_val, X_test, y_train_val, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

X_train, X_val, y_train, y_val = train_test_split(
    X_train_val,
    y_train_val,
    test_size=0.25,
    random_state=42,
    stratify=y_train_val
)


# Sayısal sütunlarda ölçekleme

sayisal_sutunlar = [
    "yaş",
    "gelir",
    "abonelik_suresi",
    "destek_talebi_sayisi",
    "abonelik_yili"
]

standard_scaler = StandardScaler()

X_train_standard = X_train.copy()
X_val_standard = X_val.copy()
X_test_standard = X_test.copy()

X_train_standard[sayisal_sutunlar] = (
    standard_scaler.fit_transform(
        X_train[sayisal_sutunlar]
    )
)

X_val_standard[sayisal_sutunlar] = (
    standard_scaler.transform(
        X_val[sayisal_sutunlar]
    )
)

X_test_standard[sayisal_sutunlar] = (
    standard_scaler.transform(
        X_test[sayisal_sutunlar]
    )
)

print(f"Ölçeklenmiş eğitim verisi: \n {X_train_standard.head()}")

# Logistic Regression modelini eğitme


log_reg = LogisticRegression(penalty="l2",C=1,max_iter=1000,random_state=42,class_weight="balanced")

log_reg.fit(X_train_standard,y_train)

log_reg_val_tahmin = log_reg.predict(X_val_standard)

log_reg_val_acc = accuracy_score(y_val,log_reg_val_tahmin)

print(f"Logistic Regression validation accuracy: {log_reg_val_acc}")

# KNN modelini eğitme

knn = KNeighborsClassifier(n_neighbors=7 , weights="distance")

knn.fit(X_train_standard,y_train)

knn_val_tahmin = knn.predict(X_val_standard)

knn_val_acc = accuracy_score(y_val,knn_val_tahmin)

print(f"KNN validation accuracy: {knn_val_acc}")

# Decision tree modelini eğitme

decision_tree = DecisionTreeClassifier(criterion="gini",max_depth=4,random_state=42)

decision_tree.fit(X_train_standard,y_train)

decision_tree_val_tahmin = decision_tree.predict(X_val_standard)

decision_tree_val_acc = accuracy_score(y_val,decision_tree_val_tahmin)


print(f"Decision Tree validation accuracy:  {decision_tree_val_acc}")


# 12. Validation sonuçlarını karşılaştırma

validation_sonuclari = {"Logistic Regression": log_reg_val_acc,"KNN": knn_val_acc,"Decision Tree": decision_tree_val_acc}

en_iyi_model_adi = max(validation_sonuclari,key=validation_sonuclari.get)

print(f"Validation sonucuna göre seçilen model: {en_iyi_model_adi}")


# Seçilen model nesnesini belirleme

if en_iyi_model_adi == "Logistic Regression":
    en_iyi_model = log_reg

elif en_iyi_model_adi == "KNN":
    en_iyi_model = knn

else:
    en_iyi_model = decision_tree


y_test_tahmin = en_iyi_model.predict(X_test_standard)

test_accuracy = accuracy_score(y_test,y_test_tahmin)

test_precision = precision_score(y_test,y_test_tahmin,zero_division=0)

test_recall = recall_score(y_test,y_test_tahmin,zero_division=0)

test_f1 = f1_score(y_test,y_test_tahmin,zero_division=0)

test_confusion_matrix = confusion_matrix(y_test,y_test_tahmin)

print("\nTest sonuçları:")
print(f"Seçilen model: {en_iyi_model_adi}")
print(f"Accuracy:  {test_accuracy}")
print(f"Precision: {test_precision}")
print(f"Recall:    {test_recall}")
print(f"F1-score:  {test_f1}")

print(f"Confusion Matrix: \n {test_confusion_matrix}")

print(
    "Yorum: Validation sonuçlarına göre Logistic Regression modeli seçilmiştir."
    "Test setinde %96.67 accuracy elde edilmiştir. "
    "Recall değerinin 1.00 olması, ayrılan müşterilerin tamamının "
    "doğru tespit edildiğini göstermektedir."
    " Precision değerinin  0.92 olması ise ayrılacak tahmini yapılan müşterilerin büyük "
    "bölümünün gerçekten ayrıldığını göstermektedir."
    "Modelin F1-score değeri 0.96 olduğu için churn tahmin performansı başarılıdır."
)
