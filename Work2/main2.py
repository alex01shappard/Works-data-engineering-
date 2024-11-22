import numpy as np
import os

# Загрузка матрицы из файла
file_path = 'data/second_task.npy'
matrix = np.load(file_path)

# Пороговое значение
threshold = 572

# Нахождение индексов элементов больше порогового значения
indices = np.argwhere(matrix > threshold)

# Создание массивов x, y, z
x = indices[:, 0]  # Индексы строк
y = indices[:, 1]  # Индексы столбцов
z = matrix[matrix > threshold]  # Значения элементов

# Сохранение массивов в формате npz
npz_path = 'outputs/2/filtered_data.npz'
compressed_npz_path = 'outputs/2/filtered_data_compressed.npz'

np.savez(npz_path, x=x, y=y, z=z)
np.savez_compressed(compressed_npz_path, x=x, y=y, z=z)

# Сравнение размеров файлов
npz_size = os.path.getsize(npz_path)
compressed_npz_size = os.path.getsize(compressed_npz_path)
diff_size = npz_size - compressed_npz_size

print(f"savez = {npz_size},", f"compressed_npz = {compressed_npz_size}")
print(f"diff = {diff_size}")
