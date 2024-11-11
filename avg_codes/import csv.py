import csv

def calculate_student_averages(filename):
    student_averages = {}
    max_score_per_exam = 100
    cap_percentage = 0.70  

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader) 
        next(reader)  

        
        for row in reader:
            if row[0] == "" or row[1] == "":
                continue  
            
            student_name = row[9]  
            scores = []
            previous_date = None

            for i in range(10, len(row) - 3):  
                score = row[i]
                current_date = headers[i]

                try:
                    score = float(score)
                except ValueError:
                    score = 0  
                
                if current_date == previous_date:
                    scores.pop()  
                scores.append(score)
                
                previous_date = current_date
            
            
            total_score = sum(scores)
            count = len([s for s in scores if s != 0])  
            if count == 0:
                average_score = 0  
            else:
                average_score = total_score / count

            max_reachable_average = max_score_per_exam * cap_percentage
            if average_score > max_reachable_average:
                average_score = max_reachable_average

            
            student_averages[student_name] = round(average_score)

    return student_averages


filename = 'exam_final.csv'  
averages = calculate_student_averages(filename)
for student, avg in averages.items():
    print(f"{student}: {avg}")
