
my_name = 'Alimhan Seidakmatov'
from csv import reader
def get_average_score(filename):
    with open(filename) as fid:
        r = reader(fid)
        '''import csv
from collections import defaultdict
file_path = 'exam_final.csv'
student_scores = defaultdict(list)
half_year_exam_scores = defaultdict(int)
final_scores = defaultdict(dict)
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  
    for row in reader:
        student_name = ""
        for i, score in enumerate(row):
            date = headers[i]
            if 'id' in date.lower():
                continue
            if 'name' in date.lower():
                student_name = score
            if date == '10/14/2024':
                half_year_exam_scores[student_name] = int(score)
            elif date not in ['Unnamed: 0', 'Unnamed: 1', 'Weekly Exam Average', 'Final Average Grade', 'Letter Grade']:
                score_value = int(score) if score.isdigit() else 0
                student_scores[student_name].append(score_value)
for student, scores in student_scores.items():
    top_6_scores = sorted(scores, reverse=True)[:7]
    average_top_6 = sum(top_6_scores) / len(top_6_scores) if top_6_scores else 0
    weighted_top_6 = average_top_6 * 0.7
    weighted_half_year = half_year_exam_scores[student] * 0.075
    final_average = weighted_top_6 + weighted_half_year
    final_scores[student]['top_6_scores'] = top_6_scores
    final_scores[student]['average_top_6'] = weighted_top_6
    final_scores[student]['midterm'] = half_year_exam_scores[student]
    final_scores[student]['final_average'] = final_average
print(half_year_exam_scores)
print("Final Scores Dictionary:")
for student, data in final_scores.items():
    print(f"{student}: Top 7: {data['top_6_scores']}, Average of top 7: {data['average_top_6']:.2f}, "
          f"Midterm: {data['midterm']}, Final Average: {data['final_average']:.2f}")'''
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