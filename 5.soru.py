import numpy as np
import pandas as pd

# Veri tablosu
data = {
    'x1': [5.1, 4.9, 7.0, 6.4, 6.3, 5.8],
    'x2': [3.5, 3.0, 3.2, 3.2, 3.3, 2.7],
    'x3': [1.4, 1.4, 4.7, 4.5, 6.0, 5.1],
    'x4': [0.2, 0.2, 1.4, 1.5, 2.5, 1.9],
    'Y': ['A', 'A', 'B', 'B', 'C', 'C']
}

df = pd.DataFrame(data)

# Özellik matrisi (X)
X = df[['x1', 'x2', 'x3', 'x4']].values

# Hedef değişken (Y)
Y = df['Y'].values

# Yeni örnek
new_example = np.array([5, 3.4, 1.5, 0.2])

# Katsayıları hesaplamak için normal denklemi kullanma
X_transpose = np.transpose(X)
X_transpose_X = np.dot(X_transpose, X)
X_transpose_Y = np.dot(X_transpose, pd.get_dummies(Y).values)  # Y'yi vektöre dönüştürme
coefficients = np.dot(np.linalg.inv(X_transpose_X), X_transpose_Y)

# Katsayılar
intercept = coefficients[0]
coefficients = coefficients[1:].flatten().tolist()




# Yeni örneği sınıflandırma
predicted_class = np.argmax(np.dot(coefficients, new_example) + intercept)
predicted_label = y_labels[predicted_class]

print("Yeni örnek sınıfı: ", predicted_label)










# Y1, Y2, Y3 tablosunu oluşturma
y_labels = df['Y'].unique()
y_classes = pd.get_dummies(df['Y']).values

df_y = pd.DataFrame(y_classes, columns=["Y" + str(i+1) for i in range(len(y_labels))])
df_final = pd.concat([df, df_y], axis=1)

print("\nGenişletilmiş Tablo:")
print(df_final)
