
from csv import reader
from collections import defaultdict

my_name = 'Yntymak Almazbek uulu'

def get_average_score(file_name):
    with open(file_name) as file:
        dat = reader(file)
        headers = next(dat)
        data = [i for i in dat if i]

    name_index = headers.index('names')
    d = defaultdict(list)

    for row in data[:-3]:
        grades = []
        student_name = row[name_index].strip()

        for index, value in enumerate(row):
            if index == 0 or index == name_index:
                continue
            
            if value == 'absent' or value == '':
                grades.append(0)
            else:
                try:
                    grades.append(float(value))
                except ValueError:
                    continue

        if student_name:
            d[student_name].extend(grades)

    finalresult = {}
    
    for student_name, grades in d.items():
        if grades:
            midterm_grade = grades[10] if len(grades) > 10 else 0
            grades_without_midterm = grades[:10] + grades[11:]

            top_grades = sorted(grades_without_midterm, reverse=True)[:7]
            
            if top_grades:
                top_average = sum(top_grades) / len(top_grades)
                final_score = (top_average * 0.7) + (midterm_grade * 0.075)
                finalresult[student_name] = round(final_score, 2)

    return tuple((student_name, score) for student_name, score in finalresult.items())


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





   