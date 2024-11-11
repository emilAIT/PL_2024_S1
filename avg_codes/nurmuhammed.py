from collections import defaultdict
import csv
my_name = 'Nurmuhammed'
from csv import reader
def get_average_score():
    with open(r"C:\Users\User\Desktop\tasks\exam_final.csv") as exam:
        slovar = defaultdict()
        slovar1 = defaultdict(int)
        exam_read = csv.reader(exam)
        n = next(exam_read)
        for i,e in enumerate(n):
            slovar[i] = e
        for e in (exam_read):
            score = []
            name = None
            for i,c in enumerate(e):
                
                if slovar[i] == "names":
                    name = c
                if (slovar[i]) =="id":
                    c = 0
                if len(slovar[i])>7:
                    try:
                        c = float(c)
                    except:
                        c = 0
                    score.append(c)
            score = sorted(score,reverse = True)
            if name:
                slovar1[name] = round(sum(score[:7])/7)*0.7
    return slovar1

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

        
