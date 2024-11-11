from csv import reader
from collections import defaultdict
def get_average_score(filename):
    with open(filename) as fid:
        file=list(reader(fid))
        head=file[0]
        file=file[1:]
        dict={}
        quezes=defaultdict(list)
        mid_id=head.index('10/14/2024')
        name_id=head.index('id')
        for line in file:
        
            name=line[name_id]
            if name not in dict:
                dict[name]=[]
            for j in line[:16]:
                if line[mid_id]:
                    pass
                if j=='absent':
                    j=0
                    dict[name].append(0)
                else:    
                    try:
                     dict[name].append(int(j))
                    except:
                        pass 

        i=0
        for j,d in enumerate(head):
            for line in file:
            #    if line[mid_id]:
            #     pass
            #    if line[name_id]:
            #     pass
               try:
                quezes[d].append(float(line[0+i]))
               except:
                pass
        i+=1
            
            # print(quezes)
        avgquezes=defaultdict(int)
        for k,v in quezes.items():
            try:
                avgquezes[k]=round(sum(v)/len(v))
            except:
                pass
        return avgquezes
print(get_average_score('exam_final.csv'))
# my_name = 'Emil Bilgazyev'
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

