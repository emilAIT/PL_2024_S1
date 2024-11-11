import csv

def calculate_average_from_csv(input_file):
    results = []
    

    with open(input_file, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)  
        
        for row in reader:
            name = row[7]  
           
            scores = row[:1] + row[2:7] + row[8:]
            
          
            numeric_scores = []
            for score in scores:
                try:
                    numeric_scores.append(float(score))
                except (ValueError, TypeError):
                   
                    numeric_scores.append(0)
            
            
            top_scores = sorted(numeric_scores, reverse=True)[:7]
            
           
            avg_score = sum(top_scores) / len(top_scores) * 0.7 if top_scores else 0 
            
            
            results.append((name, avg_score))
    
    return results
calculate_average_from_csv('exam_final.csv')

my_name = 'Emil Bilgazyev'
from csv import reader
def get_average_score(filename):
    with open(filename) as fid:
        r = reader(fid)
        '''YOUR CODE HERE'''
        ###return [(None, None)]

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
