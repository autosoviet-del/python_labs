from pathlib import Path
import csv


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает содержимое файла и возвращает его как строку.

    :param path: Путь к файлу (строка или объект Path).
    :param encoding: Кодировка файла (по умолчанию "utf-8"). Пользователь может указать другую кодировку, например, encoding="cp1251".
    :return: Строка с содержимым файла.
    :raises FileNotFoundError: Если файл не найден.
    :raises UnicodeDecodeError: Если кодировка файла несовместима с указанной.
    """
    try:
        # Открытие файла в режиме чтения и применение указанной кодировки
        with open(path, mode="r", encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        # Генерируем исключение, если файл не найден
        raise FileNotFoundError(f"Файл '{path}' не найден.")
    except UnicodeDecodeError:
        # Генерируем исключение, если возникли проблемы с кодировкой
        raise UnicodeDecodeError(f"Ошибка декодирования файла '{path}'. Проверьте кодировку.")



def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """
    Записывает данные в CSV-файл с разделителем ',', проверяя, что строки имеют одинаковую длину.

    :param rows: Данные для записи (список кортежей или списков).
    :param path: Путь к файлу (строка или объект Path).
    :param header: Заголовок CSV-файла (опциональный).
    :raises ValueError: Если строки имеют разную длину.
    """
    # Проверка, что все строки имеют одинаковую длину
    unique_row_lengths = {len(row) for row in rows}
    if len(unique_row_lengths) > 1:
        raise ValueError("Каждая строка должна иметь одинаковую длину.")

    # Открываем файл для записи
    with open(path, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # Записываем заголовок, если он задан
        if header:
            writer.writerow(header)

        # Записываем строки данных
        writer.writerows(rows)





txt = read_text("text.txt")  # должен вернуть строку
txtkor = tuple(tuple(line.split()) for line in txt.splitlines())
write_csv( txtkor, "check.csv")  # создаст CSV