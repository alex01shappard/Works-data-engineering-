import json
import msgpack
import os
from collections import defaultdict

# Загрузка данных из json
products = "data/third_task.json"
with open(products, "r", encoding="utf-8") as file:
    data = json.load(file)

# Группировка данных по имени товара и подсчет количества
aggregated_data = defaultdict(lambda: {"prices": [], "count": 0})
for item in data:
    name = item["name"]
    aggregated_data[name]["prices"].append(item["price"])
    aggregated_data[name]["count"] += 1  # Увеличиваем счетчик

# Агрегация данных (средняя, минимальная, максимальная цена)
result = {}
for name, values in aggregated_data.items():
    prices = values["prices"]
    result[name] = {
        "avg_price": sum(prices) / len(prices),
        "max_price": max(prices),
        "min_price": min(prices),
        "count": values["count"],
    }

# Сохранение результата в json
json_path = "outputs/3/aggregated_data.json"
with open(json_path, "w", encoding="utf-8") as json_out:
    json.dump(result, json_out, ensure_ascii=False, indent=4)

# Сохранение результата в msgpack
msgpack_path = "outputs/3/aggregated_data.msgpack"
with open(msgpack_path, "wb") as msgpack_out:
    msgpack.pack(result, msgpack_out)

# Сравнение размеров файлов
json_size = os.path.getsize(json_path)
msgpack_size = os.path.getsize(msgpack_path)
diff_size = json_size - msgpack_size

print(f"json file size: {json_size} bytes")
print(f"msgpack file size: {msgpack_size} bytes")
print(f"diff size: {diff_size} bytes")
