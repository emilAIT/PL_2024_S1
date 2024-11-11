from csv import reader
from collections import defaultdict

f = reader(open('exam4.csv'))
headers = next(f)
ex = list(f)

def avg_students():
    d = defaultdict(lambda: {'quiz': [], 'midterm': 0})
    name_index = headers.index('names')
    m_index = headers.index('10/14/2024')
    
    for r in ex:
        if r[name_index] != '':
            s = r[name_index]
            m = r[m_index]

            for i in range(len(r)):
                if headers[i] != 'names' and headers[i] != '10/14/2024' and headers[i] != 'id':
                    if r[i] in ['absent', '']:
                        value = 0
                    else:
                        value = float(r[i])

                    if i == m_index:
                        d[s]['midterm'] = value
                    else:
                        d[s]['quiz'].append(value)

    results = []
    for k, v in d.items():
        if len(v['quiz']) >= 7:  
            q_avg = sum(sorted(v['quiz'], reverse=True)[:7]) / 7
        else:
            q_avg = sum(v['quiz']) / len(v['quiz']) if v['quiz'] else 0 

        f_score = round((q_avg * 0.7) + (v['midterm'] * 0.075))
        results.append((k, f_score))

    return results


my_name = 'Nasipa Abdyraiymova'

from csv import reader, writer
scores = avg_students()
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