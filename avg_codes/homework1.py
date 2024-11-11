my_name = 'Atabek Aitiev'
from csv import reader
from collections import defaultdict
def get_average_score(filename):
    with open(filename) as fid:
        r = reader(fid)
        exam = [i for i in r[1:61]]
        header = r[0]    
        name_index = header.index("names")
        mid_index = header.index("10/14/2024") 
        quiz = defaultdict(list)
        mid = defaultdict(int)
        text = ''
        for i in exam:
            if i[mid_index] in ['absent', 'suspected']:
                mid[i[name_index]] = 0
            else:
                mid[i[name_index]] = int(i[mid_index])
                for item in i:
                    if item != 'absent' or item !='suspected':
                        quiz[i[name_index]].append(item)
        for key, val in quiz.items():
            for index, i in enumerate(val):
                if i == '' or i == 'absent':
                    quiz[key][index] = 0
                else:
                    try:
                        quiz[key][index] = int(i)
                    except ValueError:
                        quiz[key][index] = 0
            top = sorted(quiz[key], reverse=True)[:6]  
            if top:
                quiz[key] = sum(top) // len(top)
            else:
                quiz[key] = 0
            text += f'{key}, {round(quiz[key] * 0.70 + mid[key] * 0.075)}\n'
        return text

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