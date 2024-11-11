from csv import reader

def get_students_average(filename):
    with open('exam_final.csv', 'r') as fid:
        next(fid)  
        data = list(reader(fid))

        student_scores = {}
        
        for row in data:
            name = row[1]
            quizzes = row[2:12]  

    
            student_scores[name] = student_scores.get(name, {'quiz': []})

          
            for quiz in quizzes:
                if quiz: 
                    try:
                        quiz_score = float(quiz)  
                        student_scores[name]['quiz'].append(quiz_score)
                    except ValueError:
                        continue  
            student_scores[name]['quiz'] = sorted(student_scores[name]['quiz'], reverse=True)[:7]

     
        for student, scores in student_scores.items():
            quiz_average = sum(scores['quiz']) / len(scores['quiz']) if scores['quiz'] else 0
            yield f'{student}: {quiz_average}'

for result in get_students_average('exam_final.csv'):
    print(result)


# my_name = 'Kutman Duishenov'
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