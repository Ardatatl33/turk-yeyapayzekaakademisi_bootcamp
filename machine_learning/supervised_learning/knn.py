"""
Amaç:
  -  Göğüs kanseti veri seti kullanılarak KNN algoritmasıyla sınıflandırma yapalım
  -  Modelin doğruluk oranını hesapla, farklı K değerleri için hiperparametre araması yapalım

Plan/Program:
    1. veri setini yükle
    2. Feature ve hedef değişkenlerinin ayrılması
    3. Eğitim ve test verilerinin oluşturulması
    4. Özelliklerin ölçeklendirilmesi
    5. KNN eğitimi ve testi
    6. Doğruluk oranı ve confusion matrix
    7. Hiperparametre ayralaması
    8. Sonuçların grafiksel olarak gösterilmesi


"""

from sklearn.datasets import load_breast_cancer
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# 1. veri setini yükle

cancer = load_breast_cancer()
df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
df["target"] = cancer.target
print(df.head())


# 2. Feature ve hedef değişkenlerinin ayrılması

X = cancer.data
y = cancer.target


# 3. Eğitim ve test verilerinin oluşturulması

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.3,random_state=42)

# 4. Özelliklerin ölçeklendirilmesi

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#5. KNN eğitimi ve testi 

knn = KNeighborsClassifier(n_neighbors=12)
knn.fit(X_train,y_train)

# 6. Doğruluk oranı ve confusion matrix

y_pred = knn.predict(X_test)
acc = accuracy_score(y_test,y_pred)
print(f"Acccuracy: {acc}")

conf_matrix = confusion_matrix(y_test,y_pred)
print(f"Confusion matrix : \n {conf_matrix}")

# 7. Hiperparametre ayralaması
# 8. Sonuçların grafiksel olarak gösterilmesi

k_acc = []
k_values = []

for k in range ( 3,15):
  knn = KNeighborsClassifier(n_neighbors=k)
  knn.fit(X_train,y_train)

  y_pred = knn.predict(X_test)
  k_acc.append(accuracy_score(y_pred,y_test))
  k_values.append(k)
plt.plot(k_values,k_acc)
plt.legend()
plt.show()