my_name = 'Zhanyshbek Tynybekov'
from csv import reader
def get_average_score(filename):
    with open(filename) as file:
        file = reader(file)
        headers = next(file)
        headers = [header.strip() for header in headers]
        name_idx = headers.index("names")
        mid_idx = headers.index("10/14/2024")
        ids = headers.index("id")
        
        date_columns = [headers.index(date) for date in ['9/3/2024','10/14/2024','9/9/2024','9/11/2024','9/16/2024','9/18/2024','9/23/2024','9/24/2024','9/30/2024','10/2/2024','10/21/2024']]
        print(date_columns)
        for row in file:
            name = row[name_idx]
            scores = [float(row[i].strip()) if row[i].strip().isdigit() else 0 for i in date_columns]
            top_7_scores = sorted(scores, reverse=True)[:7]
            avg_top7 = (sum(top_7_scores) / len(top_7_scores)) * 0.7
            mid = float(row[mid_idx].strip()) if row[mid_idx].strip().isdigit() else 0
            res_mid = mid * 0.075
            final_result = avg_top7 + res_mid
            print(f"Имя: {name}, Итоговый результат: {final_result}")

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