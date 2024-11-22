"""import numpy as np

# Чтение npy файла
data = np.load("data/first_task.npy")

# Вывод данных
print(data)"""

"""file_path1 = 'outputs/1/normalized_matrix.npy'
print(np.load(file_path1).sum())"""

"""file_path = 'data/second_task.npy'
matrix = np.load(file_path)
print(matrix)"""


"""def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

print(read_json('data/third_task.json'))"""

"""import json
import sys

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# Установка UTF-8 для корректного вывода в Windows-консоли
if sys.platform == "win32":
    import os
    os.system("chcp 65001")
    sys.stdout.reconfigure(encoding="utf-8")

data = read_json('data/third_task.json')
print(json.dumps(data, indent=4, ensure_ascii=False))  # Красивый и читаемый вывод"""
import pickle
import json

# Принудительная установка utf-8 для вывода pkl-файла
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Путь к файлам
products_pkl_path = "data/fourth_task_products.json"  # Путь к pkl-файлу с товарами

with open(products_pkl_path, "rb") as pkl_file:
    products = pickle.load(pkl_file)
# Выводим изначальный pkl-файл
print(products)


