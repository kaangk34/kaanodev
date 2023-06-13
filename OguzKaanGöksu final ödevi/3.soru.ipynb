import pandas as pd
import math

data = {'X': [1,2,2,3,4,5,6,8,10,11],
        'Y': [3,5,3,9,7,2,8,6,6,1],
        'Z': ['Negatif', 'Pozitif', 'Pozitif', 'Negatif', 'Negatif', 'Pozi-tif','Pozitif','Negatif','Negatif','Negatif'],
        }

df = pd.DataFrame(data)
print("Veri Çerçevesi:")
print(df)

new_x = 7
new_y = 3

df['Öklid Mesafesi'] = df.apply(lambda row: math.sqrt((row['X'] - new_x)**2 + (row['Y'] - new_y)**2), axis=1)
print("\nÖklid Mesafeleri:")
print(df)

df['Yakınlık Sırası'] = df['Öklid Mesafesi'].rank()
print("\nYakınlık Sıraları:")
print(df)

en_yakin_3_komsu = df.nsmallest(3, 'Öklid Mesafesi')
sınıf_sayısı = en_yakin_3_komsu['Z'].value_counts()
en_yüksek_sınıf = sınıf_sayısı.idxmax()

print("\nEn yakın 3 komşu:")
print(en_yakin_3_komsu)

print("\nYeni örneğin sınıfı:", en_yüksek_sınıf)
