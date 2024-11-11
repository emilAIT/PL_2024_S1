import csv
my_name = 'Zarylbek Attokurov'
from csv import reader
def get_average_score(filename):
    with open(filename) as fid:
        r = reader(fid)
    with open('exam_final.csv') as f:
        exams = list(csv.reader(f))
        exams = exams[1:-3]
    dict = {i[9]:[] for i in exams}
    dict1 = {i[9]:'' for i in exams}
    for i in exams:
            dict[i[9]] += i[:5]
            dict[i[9]] += i[6:9]
            if i[14] == '':
                dict[i[9]] += i[10:14]
            else:
                 dict[i[9]] += i[10:13]
                 dict[i[9]] += i[14]
            dict1[i[9]] = i[1]
    dict = {name: [0 if x == '' or x == 'absent' else int(x) for x in scores] for name, scores in dict.items()}
    dict1 = {name:0 if value == 'absent' else int(value) for name, value in dict1.items()}
    dict = {name: sorted(scores)[-6:] for name, scores in dict.items()}
    for i in dict:
        dict[i] += [dict1[i]]
    finals = {}
    for i, k in dict.items():
            finals[i] = round((sum(k[:6]) / 6 * 0.7) + (k[6] * 0.075))
    print(finals)
    return [(None, None)]

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