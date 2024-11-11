from collections import defaultdict
from csv import reader

d = defaultdict(list)
with (open("exam_final.csv","r") as f):
        re = reader(f)
        header = next(re)
        names_index = header.index("names")
        id_index = header.index("id")
        midterm_index = header.index("10/14/2024")
        bonus_index = header.index("9/11/2024")
        plus_index = header.index("9/9/2024")
        for i in re:
            i[plus_index] += i[bonus_index]
            for c in i:
                if c != names_index | id_index| midterm_index| bonus_index:
                    try:
                        d[i[names_index]].append(int(c))
                    except ValueError:
                        d[i[names_index]].append(0)
            d[i[names_index]].append(i[midterm_index])
        print(d)


        def avg():
            scores = defaultdict(list)
            average = []
            for key, value in d.items():
                scores[key].append(value[-1])
                value.pop(-1)
                for _ in range(7):
                    try:
                        scores[key] = max(value)
                        value.remove(max(value))
                    except TypeError:

            return scores
        print(avg())