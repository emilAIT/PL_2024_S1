my_name = 'Aktanbek Keneshov'
from csv import reader
def calculate_scores(filename):
    results = []

    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  

            for row in reader:
                if row and len(row) > 2:
                    
                    name = row[9].strip()  
                    midterm_score = 0.0
                    
                    
                    if row[4] not in ['', 'absent']:
                        try:
                            midterm_score = float(row[4].strip())
                        except ValueError:
                            midterm_score = 0.0
                    
                    
                    quiz_scores = []
                    for score in row[5:9]:  
                        if score not in ['', 'absent']:
                            try:
                                quiz_scores.append(float(score.strip()))
                            except ValueError:
                                continue
                    
                    
                    quiz_scores.sort(reverse=True)
                    top_quiz_scores = quiz_scores[:7]
                    avg_quiz_score = sum(top_quiz_scores) / len(top_quiz_scores) if top_quiz_scores else 0
                    
                    
                    total_avg_score = (avg_quiz_score + midterm_score) / 2

                    
                    avg_quiz_score = round(avg_quiz_score, 2)
                    midterm_score = round(midterm_score, 2)
                    total_avg_score = round(total_avg_score, 2)

                    
                    results.append((name, avg_quiz_score, midterm_score, total_avg_score))

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    return results

filename = 'exam_final.csv'
scores = calculate_scores(filename)

for name, avg_quiz, midterm, total_avg in scores:
    print(f'{name}: Общий средний балл: {round(total_avg)}')


        #return [(None, None)]

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



