from csv import reader
from collections import defaultdict

def read_file(filename):
    with open(filename) as file:
        return list(reader(file))
a = 'exam_final.csv'

def get_average_score(filename):
    id = None
    read = read_file(filename)
    quiz = defaultdict(list)
    header = None
    for row in read:
        for j in range(len(row)):
            if row[j] == 'names':
                index = j
            elif row[j] == 'id':
                id = j
    
        if not header:
            header = 'kd'
            row = row[2:]
        else:   
            for i in range(len(row)):
                if row[i] != '' and index != i and i != id:
                    try:
                        es = int(row[i])
                        quiz[row[index]].append(es)
                    except:
                        quiz[row[index]].append(0)
                
                else: 
                    continue
    print(quiz)
    result = {}
    for key, value in quiz.items():
        value = sorted(value, reverse=True)[:7]
        result[key] = round(sum(value) / 7)
    ret = [(i, v)for i, v in result.items()]

    return ret
for k, v in get_average_score(a):
    print(f'{k} --> {v}')




# my_name = 'Tolonbek Abdybekov'
# from csv import reader
# def get_average_score(filename):
#     with open(filename) as fid:
#         r = reader(fid)
#         '''YOUR CODE HERE'''
#         ###return [(None, None)]

# from csv import reader, writer
# scores = get_average_score("exam4.csv")
# d = {name:score for name, score in scores}
# out = []
# with open('result.csv') as fid:
#     r = reader(fid)
#     out.append(list(next(r)) + [my_name])
#     for i in r:
#         res = i + [d.get(i[0],'')]
#         out.append(res)
# with open('result.csv', 'w', newline='') as fid:
#     w = writer(fid)
#     w.writerows(out)

