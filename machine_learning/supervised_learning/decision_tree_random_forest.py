"""
Amaç:
    - İris veri setini kullanrak karar ağacı ve random forest algoritmaları geliştirme
    - Karar ağacı görselleştirme ve öznitelik önemi inceleme 

Veri Seti:
    - İris 3 Veri seti : 3 farklı çiçek türü: setosa, versicolor, virginica
    - 4 features: sepal length, petal length, sepal with, petal with
    - 150 örnek sample var

Plan/Porgram:
    1. Veri setinin yüklenmesi
    2. feature ve target değişkenlerinin tanımlanamsı
    3. eğitim ve test veri setlerinin oluşturulması
    4. karar ağacı ve random forest modellerinin oluşturulması
    5. test verisi ile tahmin yapılması 
    6. model başarımının accuracy ile ölçülmesi
    7. karar ağacı sonuçlarının confusion matrix ile görselleştirilmesi
    9. karar ağacı feature importans incelenmesi


"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier , plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# 1. Veri setinin yüklenmesi
iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["target"] = iris.target
print(df.head(10))

#  2. feature ve target değişkenlerinin tanımlanamsı
X = iris.data
y = iris.target
#  3. eğitim ve test veri setlerinin oluşturulması

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# 4. karar ağacı ve random forest modellerinin oluşturulması

tree_clf = DecisionTreeClassifier(criterion="gini",max_depth=5,random_state=42)
random_forest_clf = RandomForestClassifier(n_estimators=100,max_depth=5,random_state=42)

tree_clf.fit(X_train,y_train)
random_forest_clf.fit(X_train,y_train)

#  5. test verisi ile tahmin yapılması 
tree_y_pred = tree_clf.predict(X_test)
random_forest_y_pred = random_forest_clf.predict(X_test)

# 6. model başarımının accuracy ile ölçülmesi
tree_acc = accuracy_score(y_test,tree_y_pred)
random_forest_acc = accuracy_score(y_test,random_forest_y_pred)

print(f"tree_acc : {tree_acc}")
print(f"random_forest_acc : {random_forest_acc}")

# 7. karar ağacı sonuçlarının confusion matrix ile görselleştirilmesi

conf_matrix = confusion_matrix(y_test, tree_y_pred)

plt.figure()
sns.heatmap(conf_matrix, annot=True, fmt = "g", cmap = "Blues", xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel("Tahmin edilen sınıf")
plt.ylabel("Gerçek sınıf")
plt.title("Karar ağacı confusion matrix")
plt.show()


# 8. karar ağacının görselleştirilmesi
plt.figure()
plot_tree(tree_clf, filled=True, feature_names=iris.feature_names, class_names = list(iris.target_names))
plt.show()

# 9. karar ağacı feature importance incelenmesi

feature_importances = tree_clf.feature_importances_
feature_names = iris.feature_names

# önem derecelerini büyükten küçüğe sırala
feature_importances_sorted = sorted(zip(feature_importances, feature_names), reverse=True)

for importance, feature_name in feature_importances_sorted:
    print(f"{feature_name}: {importance}")




