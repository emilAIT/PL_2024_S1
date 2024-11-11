import csv
from collections import defaultdict

file_path = 'exam_final.csv'
student_scores = defaultdict(list)

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Считываем заголовок
    for row in reader:
        student_name = ""
        for i, score in enumerate(row):
            header = headers[i]
            if 'name' in header.lower():
                student_name = score  # Читаем имя студента
            elif header not in ['id', 'Unnamed: 0', 'Unnamed: 1', 'Weekly Exam Average', 'Final Average Grade', 'Letter Grade']:
                # Считаем все столбцы с оценками, кроме указанных
                score_value = int(score) if score.isdigit() else 0
                student_scores[student_name].append(score_value)

# Подсчитываем среднее значение топ-7 оценок и выводим только имя и среднее
print("Names and Average of Top 7 Exam Scores:")
for student, scores in student_scores.items():
    top_7_scores = sorted(scores, reverse=True)[:7]
    average_top_7 = round(sum(top_7_scores) / len(top_7_scores), 2) if top_7_scores else 0
    print(f"{student}: {average_top_7}")

    
my_name = 'Atai Mambetov'
from csv import reader
def get_average_score(filename):
    with open(filename) as fid:
        r = reader(fid)
        '''YOUR CODE HERE'''
        ###return [(None, None)]

from csv import reader, writer
scores = get_average_score("exam4.csv")
d = {name:score for name, score in scores}
out = []
with open('result.csv') as fid:
    r = reader(fid)
    out.append(list(next(r)) + [my_name])
    for i in r:
        res = i + [d.get(i[0],'')]
        out.append(res)
with open('result.csv', 'w', newline='') as fid:
    w = writer(fid)
    w.writerows(out)



