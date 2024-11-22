import pandas as pd
import numpy as np
import json
import os
import msgpack 

# Загрузка данных
file_path = "data/bankdataset.xlsx"
data = pd.read_excel(file_path)

# Отбор столбцов
selected_columns = ["Date", "Domain", "Location", "Value", "Transaction_count"]
data = data[selected_columns]

# Преобразование даты в строку для сериализации
if 'Date' in data.columns:
    data['Date'] = data['Date'].astype(str)

# Анализ числовых данных
numeric_data = data.select_dtypes(include=[np.number])
numeric_stats = numeric_data.agg(["min", "max", "mean", "sum", "std"]).to_dict()

# Анализ категориальных данных
categorical_data = data.select_dtypes(include=["object"])
categorical_stats = {
    col: categorical_data[col].value_counts().to_dict()
    for col in categorical_data.columns
}

# Указываем путь к директории для выходных файлов
output_dir = "outputs/5"

# Сохранение расчетов в json
analysis_results = {
    "numeric_stats": numeric_stats,
    "categorical_stats": categorical_stats,
}
with open(os.path.join(output_dir, "analysis_results.json"), "w") as f:
    json.dump(analysis_results, f, indent=4)

# Сохранение данных в разных форматах
data.to_csv(os.path.join(output_dir, "dataset.csv"), index=False)
data.to_json(os.path.join(output_dir, "dataset.json"), orient="records")
data.to_pickle(os.path.join(output_dir, "dataset.pkl"))

# Сохранение в формате msgpack
with open(os.path.join(output_dir, "dataset.msgpack"), "wb") as f:
    # Преобразуем DataFrame в словарь для совместимости
    f.write(msgpack.packb(data.to_dict(orient="records"), use_bin_type=True))

# Сравнение размеров файлов
file_formats = [
    os.path.join(output_dir, "dataset.csv"),
    os.path.join(output_dir, "dataset.json"),
    os.path.join(output_dir, "dataset.pkl"),
    os.path.join(output_dir, "dataset.msgpack"),
]
file_sizes = {fmt: os.path.getsize(fmt) for fmt in file_formats}

import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Размеры файлов в байтах:")
print(file_sizes)
