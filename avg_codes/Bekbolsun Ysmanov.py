my_name = 'Bekbolsun Ysmanov'
from csv import reader
def get_average_score(filename):
    with open(filename) as fid:
        r = reader(fid)
        e = r
        e = list(e)[:61]
        header = list(e[0])
        e.remove(header)
    for i,j in enumerate(header):
        if j == 'id':
            id_index = i
        elif j=='names':
            names_index = i
        elif j == '10/14/2024':
            midterm_index = i
    quizes = []
    midterm = []
    for row in e:
        d = {}
        arr = []
        d1 = {}
        for element in row:
            if element == row[midterm_index] and (element == 'absent' or element == ''):
                d1[row[names_index]] = 0
                midterm.append(d1)
            elif element == row[midterm_index]:
                d1[row[names_index]] = int(row[midterm_index])
                midterm.append(d1)
            elif element == '' or element == 'absent':
                arr.append(0)
            elif element != row[names_index] and element != row[id_index]:
                arr.append(int(element))
        arr = sorted(arr,reverse=True)[:7]
        arr = sum(arr)/len(arr)
        d[row[names_index]] = arr
        quizes.append(d)
    result = []
    for q,m in zip(quizes,midterm):
        d = {}
        for (name,q_avg),m_grade in zip(q.items(),m.values()):
            d[name] = round(q_avg*0.7 + m_grade*0.075 + 0.01)
            result.append(d)
    return result
        ###return [(None, None)]
print(get_average_score('exam_final.csv'))

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