
my_name = 'Daniyar Karimov'
from csv import reader
def get_average_score(filename):
    with open(filename) as fid:
        r = reader(fid)
        from csv import reader
from collections import defaultdict
from csv import reader
from collections import defaultdict

def fun(file_name):
    file = list(reader(open(file_name)))
    students =file[1:60]
    student_score = defaultdict(list)
    midterm = {}
    for i in 
    for i in students:# name для удобства , m is midterm , если есть рандом то меняем на него 
        name = i[1]
        m = i[12]

            
        for score in i[2:]:
            if score == m:
                continue
            if score == 'absent' or score == '':
                score = 0
            student_score[name].append(int(score))
            
        midterm_s = i[12]
        if midterm_s == '' or midterm_s == 'absent':
            midterm_s = 0
        midterm[name] = int(midterm_s)
        
    final_score = {}
    for stud, score in student_score.items():
        avg = sum(sorted(score, reverse= True)[:6])/6
        midterm_s = midterm.get(stud, 0)
        final_s = round(0.7*avg)
        final_score[stud] = final_s
    return final_score
fun('exam_final.csv')
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