import pickle
import json

# Принудительная установка utf-8 для вывода pkl-файла
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Путь к файлам
products_pkl_path = "data/fourth_task_products.json"  # Путь к pkl-файлу с товарами
prices_json_path = (
    "data/fourth_task_updates.json"  # Путь к json-файлу с обновлениями цен
)
updated_products_pkl_path = (
    "outputs/4/updated_products.pkl"  # Путь для сохранения обновленных данных
)

"""with open(products_pkl_path, "rb") as pkl_file:
    products = pickle.load(pkl_file)
# Выводим изначальный pkl-файл
print(products)"""


# Функция обновления цены
def update_price(current_price, method, param):
    if method == "add":
        return current_price + param
    elif method == "sub":
        return current_price - param
    elif method == "percent+":
        return current_price * (1 + param)
    elif method == "percent-":
        return current_price * (1 - param)
    else:
        raise ValueError(f"Неизвестный метод обновления цены: {method}")


# Загрузка данных о товарах
with open(products_pkl_path, "rb") as pkl_file:
    products = pickle.load(pkl_file)

# Загрузка данных о новых ценах
with open(prices_json_path, "r", encoding="utf-8") as json_file:
    price_updates = json.load(json_file)

# Обновление цен
for update in price_updates:
    name = update["name"]
    method = update["method"]
    param = update["param"]

    # Поиск товара и обновление цены
    for product in products:
        if product["name"] == name:
            product["price"] = update_price(product["price"], method, param)

# Сохранение обновленных данных
with open(updated_products_pkl_path, "wb") as pkl_file:
    pickle.dump(products, pkl_file)

# Декодирование строк
"""for item in updated_products:
    for key, value in item.items():
        if isinstance(value, bytes):
            item[key] = value.decode("utf-8")"""

with open(updated_products_pkl_path, "rb") as pkl_file:
    updated_products = pickle.load(pkl_file)
# Выводим конечный pkl-файл
print(updated_products)
