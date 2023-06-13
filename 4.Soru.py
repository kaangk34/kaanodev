import pandas as pd
import numpy as np

data = np.array([15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65])
c1 = 16
c2 = 22

# Boş bir DataFrame oluşturarak tabloyu başlatma
columns = ['xi', 'c1', 'c2', 'Distance 1', 'Distance 2', 'Nearest Cluster', 'New Centroid']

for iteration in range(4):
    df = pd.DataFrame(columns=columns)
    distances_c1 = np.abs(data - c1)
    distances_c2 = np.abs(data - c2)

    nearest_cluster = np.where(distances_c1 < distances_c2, 1, 2)
    new_c1 = np.mean(data[nearest_cluster == 1])
    new_c2 = np.mean(data[nearest_cluster == 2])

    # Her iterasyonda tabloyu güncelleme
    iteration_data = np.column_stack((data, np.full_like(data, c1), np.full_like(data, c2),
                                      distances_c1, distances_c2, nearest_cluster,
                                      np.full_like(data, new_c1)))
    df = pd.DataFrame(iteration_data, columns=columns)

    # Yeni küme merkezlerini güncelleme
    c1 = new_c1
    c2 = new_c2

    # Sonuçları tablo olarak yazdırma
    print(f"Iteration {iteration + 1}:")
    print(df)
    print()
