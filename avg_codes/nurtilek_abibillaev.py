my_name = 'Nurtilek Abibillaev'
from csv import reader, writer
def get_average_score(filename):
    with open(filename) as fid:
        data = list(reader(fid)) 
        student_scores = {}
        for row in data[1:]: 
            name = row[1] 
            quizzes = row[2:12]  
            student_scores[name] = student_scores.get(name, {'quiz': []})
            for quiz in quizzes:
                try:
                    quiz_score = float(quiz) if quiz != '' else 0 
                    student_scores[name]['quiz'].append(quiz_score)
                except ValueError:
                    continue 
            student_scores[name]['quiz'].sort(reverse=True)
            student_scores[name]['quiz'] = student_scores[name]['quiz'][:7]
        for student, scores in student_scores.items():
            quiz_average = sum(scores['quiz']) / len(scores['quiz']) if scores['quiz'] else 0  
            yield f'{student}: {round(quiz_average)}'
    filename = 'exam2.csv'
    for result in get_average_score(filename):
        print(result) 
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