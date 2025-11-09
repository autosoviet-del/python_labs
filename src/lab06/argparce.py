import argparse

# Создаем парсер аргументов
parser = argparse.ArgumentParser(description="программа конвертации файлов")

# Регистрируем аргументы
parser.add_argument("--a", type=int, help="Первое число", required=True)
parser.add_argument("--b", type=int, help="Второе число", required=True)

# Разбираем аргументы
args = parser.parse_args()

# Складываем числа
sum_result = args.a + args.b

print(f"Сумма чисел равна {sum_result}")