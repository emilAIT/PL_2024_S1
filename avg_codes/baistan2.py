import csv
from csv import reader

def calculate_gpa(quizzes, midterms):
    quizzes_weight = 0.70
    midterm_weight = 0.075
    final_weight = 0.15

    quiz_avg = sum(quizzes) / len(quizzes) if quizzes else 0
    midterm_avg = sum(midterms) / len(midterms) if midterms else 0

    gpa = (quiz_avg * quizzes_weight) + (midterm_avg * midterm_weight * len(midterms))
    return gpa

def calculate_student_gpa(file, student_name):
    quiz_averages = []
    midterm_averages = []
    headers = []
    student_results = []

    with open(file, newline='') as csvfile:
        r = reader(csvfile)
        headers = next(r)
        quiz_indices = [i for i, header in enumerate(headers) if 'quiz' in header.lower()]
        midterm_indices = [i for i, header in enumerate(headers) if 'midterm' in header.lower()]

        for row in r:
            if row:
                print("Row data:", row)  # Print the entire row for structure
                student_name_normalized = student_name.strip().lower()
                student_row_name = row[0].strip().lower()  # Assuming student name is in the first column
                print("Comparing:", student_row_name, "with:", student_name_normalized)  # Debug comparison

                quizzes = [float(row[i]) for i in quiz_indices if row[i] != '']
                if len(quizzes) >= 7:
                    lowest_seven = sorted(quizzes)[:7]
                    quiz_avg = round(sum(lowest_seven) / 7, 2)
                else:
                    quiz_avg = round(sum(quizzes) / len(quizzes), 2) if quizzes else 0
                
                quiz_averages.append(quiz_avg)

                midterms = [float(row[i]) for i in midterm_indices if row[i] != '']
                midterm_avg = round(sum(midterms) / len(midterms), 2) if midterms else 0
                midterm_averages.append(midterm_avg)

                if student_row_name == student_name_normalized:
                    gpa = calculate_gpa(quizzes, midterms)
                    student_results.append(row + [quiz_avg, midterm_avg, round(gpa, 2)])

    if not student_results:
        return f"No data found for student: {student_name}"

    return headers + ['Quiz Average', 'Midterm Average', 'GPA'], student_results

file_path = 'exam_final.csv'
student_name = 'Steven Bradley'
result = calculate_student_gpa(file_path, student_name)

if isinstance(result, tuple):
    result_headers, result_data = result
    print(result_headers)
    for result_row in result_data:
        print(result_row)
else:
    print(result)








