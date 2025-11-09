from pathlib import Path
import json
import csv
import os
print("Текущая рабочая директория:", os.getcwd())
#def json_to_csvdjson_path: str, csv_path: str) -> None:

#ЧТЕНИЕ JSON
csv_path = ('scr/data/samples/people.csv')
csv_file = Path(csv_path)
json_path = ('scr/data/samples/people.json')
json_file = Path(json_path)# объект  файл с путем json_path
if not json_file.is_file(): #проверка существования файла
    raise FileNotFoundError(f"Файл {json_path} не найден.")
with json_file.open('r',encoding='utf-8') as j:
    data = json.load(j)
if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
      raise ValueError("Ожидается список словарей в JSON-файле.")
keys = set()
for entry in data:
   keys.update(entry.keys())
with open(csv_path, 'w', newline='', encoding='utf-8') as c:
    writer = csv.DictWriter(c, fieldnames=sorted(keys))  # Порядок колонок: алфавитный
    writer.writeheader()
    for entry in data:
        # Заполняем отсутствующие поля пустыми строками
        writer.writerow({key: entry.get(key, '') for key in keys})

print(data)

print(keys)