import csv

def calculate_top_students(file_path, exclude_column=3, top_n=7):
    students = []
    
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        
        for row in reader:
            student_id = row[0]
            student_name = row[1]
            if student_id.lower() == 'absent':
                continue
            
            grades = [float(row[i]) if row[i].replace('.', '', 1).isdigit() else 0 
                      for i in range(len(row)) if i != exclude_column and row[i]]
            
            if grades:
                average_grade = sum(grades) / len(grades)
                average_grade = round(average_grade)
                students.append((student_name, average_grade))
                
    top_students = sorted(students, key=lambda x: x[1], reverse=True)[:top_n]
    return top_students

file_path = 'C:/Users/Алиенора/Desktop/ait/lesson1/indepent/exam_final.csv'
top_students = calculate_top_students(file_path)

print("Топ-7 студентов по среднему баллу:")
for student in top_students:
    print(f"Имя: {student[0]}, Средний балл: {student[1]}")
#   я не знаю в какой день писали мидтерм по этому мой код игнорит один столбец с результатами экзамена. 3 столбец индекс
my_name = 'Алиенора'
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