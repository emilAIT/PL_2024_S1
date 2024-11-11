from csv import reader
from collections import defaultdict

my_name = 'Erlan Balabekov'
from csv import reader

with open('exam_final.csv') as exam_file:
    exam_read = reader(exam_file)
    header = next(exam_read)
    exam_data = list(exam_read)

names_index = header.index('names')
midterm_index = header.index('10/14/2024')

midterm = [row[midterm_index] for row in exam_data]
names = [row[names_index] for row in exam_data]

def get_average_score(exams):
    student_scores = defaultdict(list)

    for row in exams:
        if row:
            student_name = row[names_index]
            scores = row
            midterm_score = row[midterm_index]

            for score in scores:
                if score not in ['', 'absent', 'right', 'left', 'even', 'odd', 'midterm', 'Random', 'final']:
                    try:
                        score_value = float(score)
                        student_scores[student_name].append(score_value)
                    except:
                        score_value = 0

                if midterm_score not in ['', 'absent', 'right', 'left', 'even', 'odd', 'midterm', 'Random', 'final']:
                    try:
                        midterm_value = float(midterm_score)
                        student_scores[student_name].append(midterm_value)
                    except:
                        midterm_value = 0



    avg_scores = {}
    for student, scores in student_scores.items():
        top_scores = sorted(scores[:-1], reverse=True)[:7]
        avg_score = sum(top_scores) / len(top_scores)
        avg_scores[student] = avg_score * 0.7 + student_scores[student][-1] * 0.075


    return avg_scores

average_scores = get_average_score(exam_data)
print(average_scores)

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