import json
from datetime import datetime
import argparse
import time

# начальное время
start_time = time.time()

# функция сортировки
def sort_date(x):
    date = json.loads(x)['timestamp']
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

# инициализация аргументов получаемых из командной строки 
parser = argparse.ArgumentParser()
parser.add_argument('log_a', help='Path to the first file with logs')
parser.add_argument('log_b', help='Path to the second file with logs')
parser.add_argument('-o', '--output', default='logs\merge_logs.jsonl', help='Path to the end folder. Default: "logs\merge_logs.jsonl"')
args = parser.parse_args()

print('Opening files (~ 30 sec.)')

# открытие первого файла
with open(args.log_a, 'r') as file:
    text_a = file.readlines()

# открытие второго файла
with open(args.log_b, 'r') as file:
    text_b = file.readlines()

print('Merging and sorting (~ 4.5 min.)')

# объединение и сортировка
text_merge = text_a + text_b
text_merge = sorted(text_merge, key=sort_date, reverse=False)

print('Writing to the new file (~ 30 sec.)')

# запись в файл
try:
    with open(args.output, 'w') as file:
        file.writelines(text_merge)
except:
    with open(args.output + '\merge_logs.jsonl', 'w') as file:
        file.writelines(text_merge)

# конечное время
end_time = time.time()
print('Spent time: ', round((end_time - start_time)/60, 1), ' min.')

