my_name = 'Alaman Rysbekov'
from csv import reader
def get_average_score(filename):
    clas = {}
    with open(filename, "r") as file:
        fid = reader(file)
        fields = next(fid)
        data = list(fid)[:-3]
        name_id, id = fields.index("names"),fields.index("id")
    for i in data:
        clas[i[id]] =  {"name": i[name_id], "quizes":[]}
        for v in range(len(i)):
            if i[v] != "":
                try:
                    if fields[v] != name_id or fields[v] != id: 
                        if fields[v] != "10/14/2024":
                            clas[i[id]]["quizes"].append( int(i[v]))
                        else:
                            try:
                                clas[i[id]]["midterm"] = int(i[v])
                            except:
                                clas[i[id]]["midterm"] = 0
                except:
                    clas[i[id]]["quizes"].append(0) 
    for i, v in clas.items():
        clas[i]["quizes"] = sorted(clas[i]["quizes"],reverse=True)[:7]
        clas[i]["quizes"] = round(sum(clas[i]["quizes"]) / len(clas[i]["quizes"]) * 0.7 + (clas[i]["midterm"] * 0.075)) 
    return [(v["name"],v["quizes"] ) for v in clas.values() ]

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
