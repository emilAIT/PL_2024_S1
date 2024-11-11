my_name = 'Aman Anarbekov'
from csv import reader
def get_average_score(filename):
    with open(filename) as file:
        grades = []
        fid = reader(file)
        next(fid)
        for i in fid:
            if i[0] != '' and i[0] != 'right' and i[0] != 'left' :
                scores = []
                row = i[0:8] + i[10:15]
                for j in row:
                    if j != '' and j != 'absent':
                        scores.append(int(j))
                
                if i[1] != '' and i[1] != 'absent':
                    midterm = int(i[1])
                    scores.remove(midterm)
                
                scores.sort()
                top_7 = scores[-7:] 
                top = (sum(top_7) / 7) * 0.7
                mid_score = midterm * 0.075
                
                average = top + mid_score
                student_name = i[9]
                grades.append((student_name, round(average)))
        
            
                
    return grades 

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

