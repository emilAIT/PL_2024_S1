from csv import reader 

def avg_code(file):
    fid = reader(open(file))
    exam = list(fid)

    id_ind = None
    name_ind = None
    midterm_ind = None
    for i, x  in enumerate(exam[0]):  
        if x == 'id':
            id_ind = i
        if x == 'names':
            name_ind = i
        if x == '10/14/2024':
            midterm_ind = i

    d = {}
    for row in exam[1:]:
        student = row[name_ind]
        midterm = row[midterm_ind]
        id_n = row[id_ind]
        d[student] = d.get(student, {'quiz' : [],
                                    'midterm' : 0})
        for i in row:
            try:
                g = float(i)

                if i == midterm:
                    d[student]['midterm'] = g
                elif i == id_n:
                    continue
                else:
                    d[student]['quiz'].append(g)
            except ValueError:
                    pass
        d[student]['quiz'].sort(reverse=True)
    arr = []
    for k, v in d.items():
        if len(v['quiz']) >= 7:  
            quiz_average = sum(v['quiz'][:7]) / 7
        else:
            quiz_average = sum(v['quiz'])/7 if v['quiz'] else 0 

        final_score = round((quiz_average * 0.7) + (float(v['midterm']) * 0.075))
        arr.append([k, final_score])
    return arr
print(avg_code('exam_final.csv'))

my_name = 'Gulnura Onolbekova'


from csv import reader, writer
scores = avg_code("exam4.csv")
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