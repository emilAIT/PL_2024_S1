from csv import *
def calculate_average(filename):
    file=list(reader(open(filename)))[1:61]
    #data=list(reader(open(filename)))[0]
    #mid=list(reader(open(filename)))[61].index('midterm')
    #id=list(reader(open(filename)))[0].index('id')
    name=list(reader(open(filename)))[0].index('names')
    rand=list(reader(open(filename)))[61].index('Random')
    quizindex=[i for i,v in enumerate(list(reader(open(filename)))[61]) if v=='right' or v=='odd']
    out=[]
    for i in file:
        prom=[v for i,v in enumerate(i) if i in quizindex]#and i!=id]
        if i[rand]!='': prom[-1]=i[rand]
        quzlist=[i1 for i1 in ([v for i,v in enumerate(i) if i in quizindex]) if i1!='']
        quz=sorted([int(i) if i!='absent' and i!='suspected' else 0 for i in quzlist])[-7:]
        aver=round((sum(quz)/7)*0.7)#+int(i[12] if i[12]!='absent' and i[12]!='suspected' else 0)*0.075)
        out.append((i[name],aver))
    return out
print(calculate_average('exam_final.csv'))
#print(calculate_average('exam2.csv'))

my_name = 'Emil Bilgazyev'
from csv import reader
def get_average_score(filename):
    with open(filename) as fid:
        r = reader(fid)
        file=list(reader(open(fid)))[1:61]
        #data=list(reader(open(filename)))[0]
        #mid=list(reader(open(filename)))[61].index('midterm')
        #id=list(reader(open(filename)))[0].index('id')
        name=list(reader(open(fid)))[0].index('names')
        rand=list(reader(open(fid)))[61].index('Random')
        quizindex=[i for i,v in enumerate(list(reader(open(fid)))[61]) if v=='right' or v=='odd']
        out=[]
        for i in file:
            prom=[v for i,v in enumerate(i) if i in quizindex]#and i!=id]
            if i[rand]!='': prom[-1]=i[rand]
            quzlist=[i1 for i1 in ([v for i,v in enumerate(i) if i in quizindex]) if i1!='']
            quz=sorted([int(i) if i!='absent' and i!='suspected' else 0 for i in quzlist])[-7:]
            aver=round((sum(quz)/7)*0.7)#+int(i[12] if i[12]!='absent' and i[12]!='suspected' else 0)*0.075)
            out.append((i[name],aver))
        return out

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