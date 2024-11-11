import csv

# Загрузка данных из CSV файла
file_path = 'exam_final.csv'
data = []

with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    for row in reader:
        data.append(row)

# Найти индексы нужных столбцов
name_index = headers.index('names')
score_10_14_index = headers.index('10/14/2024')
score_10_21_index = headers.index('10/21/2024')
score_10_21_alt_index = headers.index('10/21/2024')
score_indices = [headers.index(date) for date in headers if '/' in date][:7]

# Преобразование данных: замена "absent" на 0 и перестановка баллов для 10/21/2024
for row in data:
    for i in range(len(row)):
        if row[i] == "absent":
            row[i] = 0
        elif i != name_index:
            try:
                row[i] = float(row[i])
            except ValueError:
                row[i] = 0

    # Перестановка баллов между столбцами 10/21/2024 и 10/21/2024.1, если оба присутствуют
    if row[score_10_21_index] > 0 and row[score_10_21_alt_index] > 0:
        row[score_10_21_index], row[score_10_21_alt_index] = row[score_10_21_alt_index], row[score_10_21_index]

# Вычисление среднего балла по заданной формуле
results = []
for row in data:
    name = row[name_index]
    max_score = max(row[i] for i in score_indices)
    score_10_14 = row[score_10_14_index]
    avg_score = (max_score * 0.7) + (score_10_14 * 0.075)
    results.append((name, round(avg_score)))

# Вывод результата
for name, avg_score in results:
    if name:  # Проверка, чтобы имя не было пустым
        print(f"({name}: {avg_score})")
