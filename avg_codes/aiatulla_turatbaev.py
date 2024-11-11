from csv import reader,QUOTE_MINIMAL
import csv

def convert_to_int(value):
    try:
        return int(value)  # Try to convert to int if possible
    except ValueError:
        return value  

def get_average(filename):
    # with open(filename) as fid:
    #     file = reader(fid)
    quizes = []
    with open(filename, "r", newline="") as file:
        reader = list(csv.reader(file, quoting=csv.QUOTE_MINIMAL))
        
        # Skip last three rows
        data_to_process = reader[:-3]
        
        # Print header
        header = data_to_process[0]
        print("Header:", header)

        for row in data_to_process:
            converted_row = [convert_to_int(cell) for cell in row]
            next(converted_row)
            for ind,i in enumerate(header):
                if i == '10/14/2024':
                    midterm = converted_row[ind]
                    # converted_row.remove(midterm)
                elif i == 'id':
                    id = converted_row[ind]
                    # converted_row.remove(id)
                elif i == 'names':
                    names = converted_row[ind]
                   
            converted_row.remove(midterm)
            converted_row.remove(id)
            converted_row.remove(names)
            for i in converted_row:
                if i == 'absent':
                    quizes.append(0)
                else:
                    quizes.append(i)
            # a = sorted(quizes)
            # print(a)
            print(quizes)
print(get_average('exam_final.csv'))

my_name = 'Aiatula Turatbaev'
from csv import reader

def convert_to_int(value):
    try:
        return int(value)  # Try to convert to int if possible
    except ValueError:
        return value  

def get_average(filename):
    # with open(filename) as fid:
    #     file = reader(fid)
    quizes = []
    with open(filename, "r", newline="") as file:
        reader = list(csv.reader(file, quoting=csv.QUOTE_MINIMAL))
        
        # Skip last three rows
        data_to_process = reader[:-3]
        
        # Print header
        header = data_to_process[0]
        print("Header:", header)

        for row in data_to_process:
            converted_row = [convert_to_int(cell) for cell in row]
            next(converted_row)
            for ind,i in enumerate(header):
                if i == '10/14/2024':
                    midterm = converted_row[ind]
                    # converted_row.remove(midterm)
                elif i == 'id':
                    id = converted_row[ind]
                    # converted_row.remove(id)
                elif i == 'names':
                    names = converted_row[ind]
                   
            converted_row.remove(midterm)
            converted_row.remove(id)
            converted_row.remove(names)
            for i in converted_row:
                if i == 'absent':
                    quizes.append(0)
                else:
                    quizes.append(i)
            # a = sorted(quizes)
            # print(a)
            print(quizes)
print(get_average('exam_final.csv'))

from csv import reader, writer
scores = get_average("exam4.csv")
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