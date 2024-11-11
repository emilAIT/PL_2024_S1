my_name = 'Nurdzhanov Ismailbek'
from csv import reader
def get_average_score(filename):
    with open(filename) as fid:
        r = reader(fid)

        '''from csv import reader
        from collections import defaultdict

        def get_average_score(file_name):
            with open(file_name) as fid:
                csv_data = reader(fid)
                header = next(csv_data)
                data = list(csv_data)[:-3] 

            id_index = header.index("id")
            names_index = header.index("names")
            midterm_index = header.index("10/14/2024")  

            student_data = defaultdict(lambda: {'quiz': [], 'midterm': []})

            for row in data:
                student_name = row[names_index]
                
                quiz_scores = []
                
                for i, value in enumerate(row):
                    if i == id_index or i == names_index:
                        continue

                    score = int(value) if value not in ('absent', '') else 0

                    if i == midterm_index:
                        student_data[student_name]['midterm'].append(score)
                    else:
                        quiz_scores.append(score)
                
                student_data[student_name]['quiz'].extend(quiz_scores)

            for student, scores in student_data.items():
                top_7_quiz_average = sum(sorted(scores['quiz'], reverse=True)[:7]) / 7
                midterm_total = sum(scores['midterm'])
                
                final_score = round(top_7_quiz_average * 0.7 + midterm_total * 0.075)
                
                print(f'{student}: {final_score}')

        file_name = "exam_final.csv"
        get_average_score(file_name)'''

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