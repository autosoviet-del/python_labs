from pathlib import Path
import json
import csv

def json_to_csv(json_path:str, csv_path:str) -> None:
    json_file = Path(json_path)  # объект  файл с путем json_path
    #if not json_file.is_file():  # проверка существования файла
    #   raise FileNotFoundError(f"Файл {json_path} не найден.")
    try:
        with json_file.open('r', encoding='utf-8') as j:
            data = json.load(j)
    #if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
    #   raise ValueError("Ошибка формата")
    except FileNotFoundError:
        print(f"Файл {json_path} не найден.")
    except ValueError:
        print("Ошибка формата")
    keys = set()
    for el in data:#проходим по всем элементам data
        keys.update(el.keys())#записываем все ключи в  keys
    with open(csv_path, 'w', newline='', encoding='utf-8') as c:
        writer = csv.DictWriter(c, fieldnames=sorted(keys))  # Порядок колонок: алфавитный
        writer.writeheader()
        for entry in data:
            writer.writerow({key: entry.get(key, '') for key in keys})


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path(csv_path)
    if not csv_file.is_file():
        raise FileNotFoundError(f"Файл {csv_path} не найден")
    csv_data = []#пустой список словарей
    with csv_file.open('r', encoding='utf-8') as c:
        reader = csv.DictReader(c)
        for row in reader:
            csv_data.append(row)#добавляем ряд
    if not csv_data:#проверка пусто или none
        raise ValueError("Файл пуст или плохо сформирован.")
    with open(json_path, 'w', encoding='utf-8') as j:
        json.dump(csv_data, j, ensure_ascii=False, indent=4)

#Тесты
js='data/out/people1.json'
cs='data/samples/people.csv'
csv_to_json(cs, js)
json_to_csv('data/samples/people.json', 'data/out/people1.csv')
