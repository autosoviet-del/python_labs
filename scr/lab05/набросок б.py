import csv
from openpyxl import Workbook
from pathlib import Path
csv_file=Path('scr/data/samples/cities.csv')
with csv_file.open('r', encoding='utf-8') as c:
    reader = csv.reader(c)
    rows=list(reader)
    print(rows)
if not rows or not rows[0]:
    raise ValueError("Пустой CSV или неправильный формат.")
wb = Workbook()
ws = wb.active
ws.title = 'Sheet1'
for row in rows:
    ws.append(row)
for column_cells in ws.columns:
       max_length = 0
       for cell in column_cells:
           value_len = len(str(cell.value)) if cell.value else 0
           max_length = max(value_len, max_length)
       adjusted_width = max(max_length + 2, 8)  # Добавляем пару символов и устанавливаем минимум 8 символов
       ws.column_dimensions[column_cells[0].column_letter].width = adjusted_width
wb.save('scr/data/out/xlsx_path.xlsx')
