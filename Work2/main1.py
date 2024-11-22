import numpy as np
import json

# Загрузка матрицы из файла
file_path = 'data/first_task.npy'
matrix = np.load(file_path)

# Вычисления
matrix_sum = np.sum(matrix)
matrix_avg = np.mean(matrix)
main_diag = np.diag(matrix)
sec_diag = np.diag(np.fliplr(matrix))

sum_main_diag = np.sum(main_diag)
avg_main_diag = np.mean(main_diag)
sum_sec_diag = np.sum(sec_diag)
avg_sec_diag = np.mean(sec_diag)

matrix_max = np.max(matrix)
matrix_min = np.min(matrix)

# Формирование данных для json
results = {
    "sum": float(matrix_sum),
    "avr": float(matrix_avg),
    "sumMD": float(sum_main_diag),
    "avrMD": float(avg_main_diag),
    "sumSD": float(sum_sec_diag),
    "avrSD": float(avg_sec_diag),
    "max": float(matrix_max),
    "min": float(matrix_min)
}

# Сохранение json
json_path = 'outputs/1/matrix_results.json'
with open(json_path, 'w') as json_file:
    json.dump(results, json_file, indent=4)

# Нормализация матрицы
normalized_matrix = matrix / matrix_sum
normalized_matrix_path = 'outputs/1/normalized_matrix.npy'
np.save(normalized_matrix_path, normalized_matrix)

json_path, normalized_matrix_path

file_path1 = 'outputs/1/normalized_matrix.npy'
print(np.load(file_path1).sum())
