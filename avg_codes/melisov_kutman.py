from csv import reader, writer
from collections import defaultdict

file_name = "exam_final.csv"

my_name = 'Kutman Melisov'


def get_average_score(file_name):
    with open(file_name) as fid:
        csv_data = reader(fid)
        header = next(csv_data)
        data = list(csv_data)

    data = data[:-3]

    d = defaultdict(dict)

    id_index = 0
    names_index = 0
    midterm_index = 0
    for i, value in enumerate(header):
        if value == "id":
            id_index = i
        if value == "names":
            names_index = i
        if value == "10/14/2024":
            midterm_index = i

    for row in data:

        d[row[names_index]]['quiz'] = d[row[names_index]].get('quiz', [])
        d[row[names_index]]['midterm'] = d[row[names_index]].get('midterm', [])
        d[row[names_index]]['total'] = d[row[names_index]].get('total', 0)

        quiz_data = []

        for i, value in enumerate(row):
            if i != names_index and i != id_index:
                if value == 'absent' or value == '':
                    value = '0'

                if i == midterm_index:
                    d[row[names_index]]['midterm'].append(int(value))
                    continue

                quiz_data.append(int(value))

        d[row[names_index]]['quiz'].extend(quiz_data)

        quizes = sum(sorted(d[row[names_index]]['quiz'], reverse=True)[:7]) / 7
        midterm = sum(d[row[names_index]]['midterm'])

        total_score = round(quizes * 0.7 + midterm * 0.075)
        d[row[names_index]]['total'] = total_score

    final_data = []
    for name in d:
        final_data.append((name, d[name]['total']))

    return final_data


scores = get_average_score("exam4.csv")
d = {name: score for name, score in scores}
out = []
with open('result.csv') as fid:
    r = reader(fid)
    out.append(list(next(r)) + [my_name])
    for i in r:
        res = i + [d.get(i[0], '')]
        out.append(res)
with open('result.csv', 'w', newline='') as fid:
    w = writer(fid)
    w.writerows(out)