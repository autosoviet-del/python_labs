import sys
from pathlib import Path

# Путь к файлу
csv_file = Path('data/samples/people.csv')

try:
    with open(csv_file, mode='r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            line = line.rstrip('\n\r')
            # Используем 🐍 и разделитель, но аккуратно
            print(f"🐍 {line_num:3d} ▸ {line}")

except FileNotFoundError:
    print(f"❌ Ошибка: файл не найден — {csv_file.resolve()}", file=sys.stderr)
    sys.exit(1)

except PermissionError:
    print(f"🔒 Ошибка: нет прав на чтение — {csv_file.resolve()}", file=sys.stderr)
    sys.exit(1)

except UnicodeDecodeError:
    print(f"❗ Ошибка: файл не в UTF-8 — {csv_file.resolve()}", file=sys.stderr)
    sys.exit(1)

except Exception as e:
    print(f"💥 Неизвестная ошибка: {e}", file=sys.stderr)
    sys.exit(1)
