from pathlib import Path
import sys 

csv_file = Path('data/samples/people.csv')

try:
    with open(csv_file, mode='r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            line = line.rstrip('\n\r')
            print(line)

except FileNotFoundError:
    print(f"❌ Файл не найден: {csv_file.resolve()}", file=sys.stderr)
    sys.exit(1)

except PermissionError:
    print(f"🔒 Нет прав на чтение файла: {csv_file.resolve()}", file=sys.stderr)
    sys.exit(1)

except Exception as e:
    print(f"❗ Неизвестная ошибка: {e}", file=sys.stderr)
    sys.exit(1)
